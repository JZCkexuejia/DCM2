from PyQt5.QtWidgets import QMainWindow, QMessageBox, QSpinBox, QDoubleSpinBox, QComboBox

from custom_widgets.py_toggle import PyToggle
from handlers.connection import ConnectionHandler, PacemakerState

# Dashboard controller class that will handle all the events of the widgets in the dashboard view
from handlers.graphs import GraphsHandler
from handlers.parameters import ParametersHandler
import numpy as np
from views.dcm_interface import Ui_DCMInterface


class DCMInterface(QMainWindow, Ui_DCMInterface):
    def __init__(self, parent):
        super(DCMInterface, self).__init__()
        self.username = None
        self.pace_mode = "AOO"
        self.user_params = {}
        self.parent = parent

        self.current_conn_status = PacemakerState.NOT_CONNECTED

        self.atrial_toggle = PyToggle()
        self.ventricular_toggle = PyToggle()
        self.atrial_toggle.setChecked(False)
        self.ventricular_toggle.setChecked(False)

        self._params = ParametersHandler()
        self._conn = ConnectionHandler()

        self.setupUi(self)
        self._graphs = GraphsHandler(self.atrial_plots, self.ventricular_plots)
        
        # Start connection thread
        self._conn.connect_status_change.connect(self.handle_pace_conn)
        self._conn.serial.ecg_data_update.connect(self._graphs.update_data)
        self._conn.serial.params_received.connect(self._show_alert)


    @staticmethod
    def _show_alert(success: bool, msg: str) -> None:
        """
        Displays an error message with the specified text
        :param msg: the text to show
        """
        qm = QMessageBox()
        if success:
            QMessageBox.information(qm, "Connection", msg, QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(qm, "Connection", msg, QMessageBox.Ok, QMessageBox.Ok)

    # Upon successful pacemaker connection, update the status bar animation and the About window table
    def handle_pace_conn(self, conn_state: PacemakerState, msg: str) -> None:
        self.statusBar.handle_conn_anim(conn_state, msg)
        self.current_conn_status = conn_state
        if self.current_conn_status == PacemakerState.REGISTERED:
            self.atrial_toggle.setEnabled(True)
            self.ventricular_toggle.setEnabled(True)
        else:
            self.atrial_toggle.setEnabled(False)
            self.ventricular_toggle.setEnabled(False)
            self.atrial_toggle.setChecked(False)
            self.ventricular_toggle.setChecked(False)

    # to initialize the dashboard view after login for a particular user
    def init(self, username):
        self._conn.start()
        self.username = username
        self.label_welcome.setText("Welcome, {}".format(self.username))
        self._params.update_params_on_user_auth(username)

        self.user_params = self._params.get_user_params()
        for key, value in self.user_params.items():
            param_input = self.__getattribute__("param_{}".format(key.replace(" ", "_").lower()))
            if isinstance(param_input, QSpinBox):
                param_input.setValue(int(value))
            elif isinstance(param_input, QDoubleSpinBox):
                param_input.setValue(float(value))
            else:
                param_input.setCurrentText(value)

        self.mode_AOO.setChecked(True)

    # function overriding, setupUi function setup call for widgets
    def setupUi(self, DCMInterface):
        Ui_DCMInterface.setupUi(self, DCMInterface)

        # click handlers of the buttons in the ui
        self.btn_logout.clicked.connect(self.onclick_btn_logout)
        #self.btn_settings.clicked.connect(self.onclick_btn_settings)

        self.frame_plots_checks.hide()
        # show or hide the plots, depending on whether or not the toggle is active, when it changes state
        self.frame_atrial.layout().addWidget(self.atrial_toggle)
        self.frame_ventricular.layout().addWidget(self.ventricular_toggle)
        self.atrial_toggle.stateChanged.connect(self.plots_toggled)
        self.ventricular_toggle.stateChanged.connect(self.plots_toggled)

        self.mode_AOO.toggled.connect(self.pacing_mode_changed)
        self.mode_VOO.toggled.connect(self.pacing_mode_changed)
        self.mode_AAI.toggled.connect(self.pacing_mode_changed)
        self.mode_VVI.toggled.connect(self.pacing_mode_changed)
        self.mode_DOO.toggled.connect(self.pacing_mode_changed)
        self.mode_AOOR.toggled.connect(self.pacing_mode_changed)
        self.mode_VOOR.toggled.connect(self.pacing_mode_changed)
        self.mode_AAIR.toggled.connect(self.pacing_mode_changed)
        self.mode_VVIR.toggled.connect(self.pacing_mode_changed)
        self.mode_DOOR.toggled.connect(self.pacing_mode_changed)

        self.btn_transmit_data.clicked.connect(self.transmit_data)
        self.btn_update_params.clicked.connect(self.update_params)
        self.btn_reset_defaults.clicked.connect(self.reset)

        # on value changed of each param, validate their values
        for param_name in self._params.get_params_names():
            param = self.__getattribute__("param_{}".format(param_name.replace(" ", "_").lower()))
            if isinstance(param, QSpinBox) or isinstance(param, QDoubleSpinBox):
                param.valueChanged.connect(
                    self.validate_params
                )
            if isinstance(param, QDoubleSpinBox):
                param.setDecimals(1)

    def closest_multiple(self, n, x):
        if x > n:
            return x
        z = (int)(x / 2)
        n = n + z
        n = n - (n % x)
        return n

    def validate_params(self):
        self.param_maximum_sensor_rate.setMaximum(self.param_upper_rate_limit.value())
        if self.sender() == self.param_lower_rate_limit:
            # 30-50
            if 30 <= self.param_lower_rate_limit.value() <= 50:
                self.param_lower_rate_limit.setSingleStep(5)
            # 50-90
            if 51 <= self.param_lower_rate_limit.value() <= 89:
                self.param_lower_rate_limit.setSingleStep(1)
            # 90-175
            if 90 <= self.param_lower_rate_limit.value() <= 175:
                self.param_lower_rate_limit.setSingleStep(5)

        if isinstance(self.sender(), QSpinBox) or isinstance(self.sender(), QDoubleSpinBox):
            if int(self.sender().value() % self.sender().singleStep()) != 0:
                self.sender().setValue(self.closest_multiple(self.sender().value(), self.sender().singleStep()))

    def reset(self):
        self._params.reset()
        self.user_params = self._params.get_user_params()
        for key, value in self.user_params.items():
            param_input = self.__getattribute__("param_{}".format(key.replace(" ", "_").lower()))
            if isinstance(param_input, QSpinBox):
                param_input.setValue(int(value))
            elif isinstance(param_input, QDoubleSpinBox):
                param_input.setValue(float(value))
            else:
                param_input.setCurrentText(value)

    def update_params(self):
        for key, value in self.user_params.items():
            param_input = self.__getattribute__("param_{}".format(key.replace(" ", "_").lower()))
            if isinstance(param_input, QComboBox):
                self.user_params[key] = param_input.currentText()
            else:
                self.user_params[key] = str(param_input.value())
        self._params.confirm(self.user_params)

    def transmit_data(self):
        self.update_params()
        self._conn.send_data_to_pacemaker(self._params.get_params(self.pace_mode))
    
    def pacing_mode_changed(self):
        self.pace_mode = self.sender().text()
        mode_params = self._params.filter_params(self.pace_mode)
        # hide all param frames
        for param_name in self._params.get_params_names():
            self.__getattribute__("frame_{}".format(param_name.replace(" ", "_").lower())).hide()
        for key, value in mode_params.items():
            if key != "Pacing Mode":
                self.__getattribute__("frame_{}".format(key.replace(" ", "_").lower())).show()

    def plots_toggled(self):
        self._conn.printgraph(self.atrial_toggle.isChecked(), self.ventricular_toggle.isChecked())

    # click event of logout button
    def onclick_btn_logout(self):
        self.atrial_toggle.setChecked(False)
        self.ventricular_toggle.setChecked(False)
        self._conn.printgraph(False, False)
        self._graphs._atri_data = np.array([])
        self._graphs._vent_data = np.array([])
        self._graphs.index = 0
        self.hide()
        self.parent.show()

    # # click event of settings button
    # def onclick_btn_settings(self):
    #     # the functionality for the settings button can be later implemented here
    #     pass

    def reset_parameters(self):
        self.frame_atrial_amplitude.hide()
        self.frame_atrial_pulses_width.hide()
        self.frame_atrial_refractory_period.hide()
        self.frame_atrial_sensitivity.hide()
        self.frame_hysteresis.hide()
        self.frame_lower_rate_limit.hide()
        self.frame_rate_smoothing.hide()
        self.frame_upper_rate_limit.hide()
        self.frame_ventricular_amplitude.hide()
        self.frame_ventricular_pulse_width.hide()
        self.frame_ventricular_refractory_period.hide()
        self.frame_ventricular_sensitivity.hide()