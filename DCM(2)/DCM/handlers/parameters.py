import json
from json import JSONDecodeError
from typing import Dict, List, Union

from PyQt5.QtWidgets import QMessageBox, QTableWidget


# This class handles the parameters for the DCM
class ParametersHandler:
    _params_per_mode: Dict[str, List[str]]
    _default_params_store: Dict[str, str]
    _user_params_store: Dict[str, str]
    _username: str
    _params_store: Dict[str, Dict[str, str]]

    _PARAMETERS_FILE_PATH = "parameters.json"

    def __init__(self):
        print("Parameters handler init")

        self._default_params_store = {
            "Lower Rate Limit": '60',
            "Upper Rate Limit": '120',
            "Maximum Sensor Rate": '120',
            "Fixed AV Delay": '150',
            "Atrial Amplitude": '5',
            "Atrial Pulse Width": '1',
            "Atrial Sensitivity": '1',
            "Ventricular Amplitude": '5',
            "Ventricular Pulse Width": '1',
            "Ventricular Sensitivity": '2.5',
            "ARP": '250',
            "VRP": '320',
            "PVARP": '250',
            "Activity Threshold": "Med",
            "Reaction Time": '30',
            "Response Factor": '8',
            "Recovery Time": '5'
        }

        # Create dictionary of parameters per pacing mode
        self._params_per_mode = {
            'AOO':  ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width"],
            'VOO':  ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width"],
            'AAI':  ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width",
                    "Atrial Sensitivity", "ARP", "PVARP"],
            'VVI':  ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width",
                    "Ventricular Sensitivity", "VRP"],
            'AOOR': ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude",
                     "Atrial Pulse Width", "Activity Threshold", "Reaction Time", "Response Factor",
                     "Recovery Time"],
            'VOOR': ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Ventricular Amplitude",
                     "Ventricular Pulse Width", "Activity Threshold", "Reaction Time", "Response Factor",
                     "Recovery Time"],
            'AAIR': ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude",
                     "Atrial Pulse Width", "Atrial Sensitivity", "ARP", "PVARP", "Activity Threshold", "Reaction Time",
                     "Response Factor", "Recovery Time"],
            'VVIR': ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Ventricular Amplitude",
                     "Ventricular Pulse Width", "Ventricular Sensitivity", "VRP", "Activity Threshold", "Reaction Time",
                     "Response Factor", "Recovery Time"],
            'DOO':  ["Lower Rate Limit", "Upper Rate Limit", "Fixed AV Delay", "Atrial Amplitude", "Atrial Pulse Width",
                    "Ventricular Amplitude", "Ventricular Pulse Width"],
            'DOOR': ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Fixed AV Delay",
                     "Atrial Amplitude", "Atrial Pulse Width", "Ventricular Amplitude", "Ventricular Pulse Width",
                     "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]}

        # Create list of values for Activity Threshold
        self._act_thresh = ["V-Low", "Low", "Med-Low", "Med", "Med-High", "High", "V-High"]

        # Dict that stores the parameters for a specific user (stored in username), keys are the parameter name,
        # values are the param value
        self._user_params_store = {}
        self._username = ""

        # Try and optionally load existing parameters from file and update GUI with those saved values
        self._params_store = {}
        try:
            with open(self._PARAMETERS_FILE_PATH, mode='r') as f:
                self._params_store.update(json.load(f))
        except (FileNotFoundError, JSONDecodeError):
            pass

    # Update the parameter values to the user-specific ones based on the user that is authenticated
    def update_params_on_user_auth(self, username: str):
        self._username = username
        self._user_params_store = self._params_store.get(username, self._default_params_store)
        return self._user_params_store

    # When confirm is clicked, update param store and write the values to file
    def confirm(self, params) -> None:
        self._user_params_store = {key: f"{value}" for key, value in params.items()}
        self._update_params_file()

    # When reset is clicked, prompt user if they're sure, and optionally load GUI defaults and update file and GUI
    def reset(self) -> None:
        qm = QMessageBox()
        response = QMessageBox.question(qm, "Parameters", "Are you sure you want to reset all the values?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if response == QMessageBox.Yes:
            self._user_params_store = self._default_params_store
            self._update_params_file()

    def get_user_params(self):
        return self._user_params_store

    # Return a pacing mode dependent dict of parameters with the names as keys, and param values with units as values
    def filter_params(self, pace_mode: str) -> Dict[str, str]:
        mode_params = {key: f"{self._user_params_store[key]}" for key in
                       self._params_per_mode[pace_mode]}
        mode_params["Pacing Mode"] = pace_mode
        return mode_params

    def get_params_names(self):
        return self._default_params_store.keys()

    # Write params store to file, creating a new one if it doesn't exist
    def _update_params_file(self) -> None:
        with open(self._PARAMETERS_FILE_PATH, mode='w+') as f:
            self._params_store[self._username] = self._user_params_store
            json.dump(self._params_store, f)

    # Return all the parameters, casted to their respective data type
    def get_params(self, pace_mode: str) -> Dict[str, Union[int, float]]:
        typed_params = {"Pacing Mode": list(self._params_per_mode.keys()).index(pace_mode)}
        for key, value in self._user_params_store.items():
            try:
                typed_params[key] = int(value)
            except:
                try:
                    typed_params[key] = int(float(value) * 20)
                except:
                    typed_params[key] = self._act_thresh.index(value) + 1
        return typed_params
