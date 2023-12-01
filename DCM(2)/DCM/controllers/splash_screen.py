from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from controllers.login_register import LoginRegister
from views.splash_screen import Ui_SplashScreen

# Global values
progressBarValue = 0


# Dashboard controller class that will handle all the events of the widgets in the dashboard view
class SplashScreen(QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setupUi(self)

    # function overriding, setupUi function setup call for widgets
    def setupUi(self, SplashScreen):
        Ui_SplashScreen.setupUi(self, SplashScreen)

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(10)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Apply shadow to central widget
        self.centralwidget.setGraphicsEffect(self.shadow)

        # Lets use QTIMER to delay the progressBar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.appProgress)

        self.timer.start(1)

    # this function will change the value of the progress bar iteratively
    def appProgress(self):
        # Acess the global variable progressBarValue
        global progressBarValue

        # Apply progressBarValue to the progressBar
        self.my_progressBar.setValue(progressBarValue)

        if progressBarValue == 49:
            self.my_progressBar.setStyleSheet(self.my_progressBar.styleSheet().replace("color:white;", "color:black;"))

        if progressBarValue > 100:
            # reset / stop timer
            self.timer.stop()
            self.close()

            self.login_register = LoginRegister()
            self.login_register.show()

        progressBarValue += 1