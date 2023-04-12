import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog
from lakeshore_controller import LakeShoreController
from keithley_controller import KeithleyController
from ips120_controller import IPS120Controller
from curve_fitting import fit_curve
from data_conversion import convert_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create instances of the subprogram classes
        self.lakeshore = LakeShoreController("GPIB::1")
        self.keithley = KeithleyController("GPIB::12")
        self.ips = IPS120Controller("GPIB::25")

        # Create labels and line edits for user input
        self.lbl_temp_setpoint = QLabel("Temperature Setpoint (K):", self)
        self.lbl_temp_setpoint.move(50, 50)
        self.le_temp_setpoint = QLineEdit(self)
        self.le_temp_setpoint.move(200, 50)

        self.lbl_current_setpoint = QLabel("Current Setpoint (A):", self)
        self.lbl_current_setpoint.move(50, 100)
        self.le_current_setpoint = QLineEdit(self)
        self.le_current_setpoint.move(200, 100)

        self.lbl_field_setpoint = QLabel("Magnetic Field Setpoint (T):", self)
        self.lbl_field_setpoint.move(50, 150)
        self.le_field_setpoint = QLineEdit(self)
        self.le_field_setpoint.move(200, 150)

        # Create buttons for each subprogram
        self.btn_lakeshore = QPushButton("Measure Temperature", self)
        self.btn_lakeshore.move(50, 200)
        self.btn_lakeshore.clicked.connect(self.measure_temperature)

        self.btn_keithley = QPushButton("Measure Current", self)
        self.btn_keithley.move(50, 250)
        self.btn_keithley.clicked.connect(self.measure_current)

        self.btn_ips = QPushButton("Set Magnetic Field", self)
        self.btn_ips.move(50, 300)
        self.btn_ips.clicked.connect(self.set_magnetic_field)

        self.btn_curve_fit = QPushButton("Curve Fitting", self)
        self.btn_curve_fit.move(50, 350)
        self.btn_curve_fit.clicked.connect(self.curve_fit)

        self.btn_data_conversion = QPushButton("Convert Data", self)
        self.btn_data_conversion.move(50, 400)
        self.btn_data_conversion.clicked.connect(self.convert_data)

        # Create a label for displaying the temperature, current, and magnetic field
        self.lbl_display = QLabel(self)
        self.lbl_display.move(400, 50)
        self.lbl_display.resize(300, 300)

    def measure_temperature(self):
        # Get the temperature setpoint from the line edit
        temp_setpoint = float(self.le_temp_setpoint.text())
        # Call the measure_temperature method of the LakeShoreController
        temperature = self.lakeshore.measure_temperature(temp_setpoint)
        # Display the temperature in the GUI
        self.lbl_display.setText(f"Temperature: {temperature} K")

    def measure_current(self):
        # Get the current setpoint from the line edit
        current_setpoint = float(self.le_current_setpoint.text())
        # Call the measure_current method of the KeithleyController
        current = self.keithley.measure_current(current_setpoint)
        # Display the current in the GUI
        self.lbl_display.setText(f"Current: {current} A")

    def set_magnetic_field(self):
        # Get the magnetic field setpoint from the line edit
        field_setpoint = float(self.le_field_setpoint.text())
        # Call the set_magnetic_field method of the IPS120Controller
        self.ips.set_magnetic_field(field_setpoint)
        # Display the current magnetic field in the GUI
        self.lbl_display.setText(f"Magnetic Field: {field_setpoint} T")

    def curve_fit(self):
        # Get the data to fit from the user, using a file dialog
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_():
            filename = file_dialog.selectedFiles()[0]
            data = np.loadtxt(filename)
            # Fit the data using the fit_curve function from curve_fitting.py
            params = fit_curve(data)
            # Display the fitted parameters in the GUI
            self.lbl_display.setText(f"Fitted Parameters: {params}")

    def convert_data(self):
        # Get the data to convert from the user, using a file dialog
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_():
            filename = file_dialog.selectedFiles()[0]
            data = np.loadtxt(filename)
            # Convert the data using the convert_data function from data_conversion.py
            convert_data(data)
            # Display a message in the GUI indicating the conversion is complete
            self.lbl_display.setText("Data conversion complete.")

        #
