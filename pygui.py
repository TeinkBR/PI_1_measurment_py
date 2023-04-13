import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog
from PyQt5.QtCharts import QChart, QChartView, QLineSeries
from Lakeshore_336_Temperature_controller import LakeShoreController
from Keithley2182_nanovoltmeter import KeithleyController
from Keithley_2612_B_System_source_meter import IPS120Controller
from curve_fit import fit_curve
from data_conversion import convert_data
from oxford_instruments_ips_120_10_superconducting_magnet import MagnetController
from mock_measurement import MockMeasurement
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # mock measurement
        self.btn_measure = QPushButton("Measure", self)
        self.btn_measure.move(50, 200)
        self.btn_measure.clicked.connect(self.measure)

        # Create a chart view widget
        self.chart_view = QChartView(self)
        self.chart_view.move(400, 400)
        self.chart_view.resize(300, 200)

        # Create line series for current vs feedback
        self.series = QLineSeries()
        self.series.setName("Current vs Feedback")
        self.chart_view.chart().addSeries(self.series)

        self.mock_measurement = MockMeasurement()

        # Create instances of the subprogram classes
        self.lakeshore = LakeShoreController("GPIB::1")
        self.keithley = KeithleyController("GPIB::12")
        self.ips = IPS120Controller("GPIB::25")
        self.magnet_controller = MagnetController()

        self.btn_lakeshore.setFixedSize(200, 50)
        self.setFixedSize(800, 600)

        # Create a chart view widget
        self.chart_view = QChartView(self)
        self.chart_view.move(400, 400)
        self.chart_view.resize(300, 200)

        # Create line series for magnetic field vs resistance and current vs voltage
        self.series1 = QLineSeries()
        self.series1.setName("Magnetic Field vs Resistance")
        self.chart_view.chart().addSeries(self.series1)

        self.series2 = QLineSeries()
        self.series2.setName("Current vs Voltage")
        self.chart_view.chart().addSeries(self.series2)

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

        self.btn_sweep_field = QPushButton("Sweep Magnetic Field", self)
        self.btn_sweep_field.move(50, 450)
        self.btn_sweep_field.clicked.connect(self.sweep_m)
        self.btn_data_conversion = QPushButton("Convert Data", self)
        self.btn_data_conversion.move(50, 400)
        self.btn_data_conversion.clicked.connect(self.convert_data)

        # Create buttons for setting magnetic field
        self.btn_set_magnetic_field = QPushButton("Set Magnetic Field", self)
        self.btn_set_magnetic_field.move(50, 450)
        self.btn_set_magnetic_field.clicked.connect(self.set_magnetic_field)

        self.btn_sweep_magnetic_field = QPushButton("Sweep Magnetic Field", self)
        self.btn_sweep_magnetic_field.move(50, 500)
        self.btn_sweep_magnetic_field.clicked.connect(self.sweep_magnetic_field)

        # Create labels and line edits for user input
        self.lbl_field_setpoint = QLabel("Magnetic Field Setpoint (T):", self)
        self.lbl_field_setpoint.move(400, 50)
        self.le_field_setpoint = QLineEdit(self)
        self.le_field_setpoint.move(550, 50)

        self.lbl_field_range = QLabel("Magnetic Field Range (T):", self)
        self.lbl_field_range.move(400, 100)
        self.le_field_range = QLineEdit(self)
        self.le_field_range.move(550, 100)

        self.lbl_num_points = QLabel("Number of Points:", self)
        self.lbl_num_points.move(400, 150)
        self.le_num_points = QLineEdit(self)
        self.le_num_points.move(550, 150)

        # Create a label for displaying the magnetic field
        self.lbl_display_magnetic_field = QLabel(self)
        self.lbl_display_magnetic_field.move(400, 200)
        self.lbl_display_magnetic_field.resize(300, 50)



    def sweep_magnetic_field(self):
        # Get the magnetic field range and number of points from the line edits
        field_range = tuple(map(float, self.le_field_range.text().split(",")))
        num_points = int(self.le_num_points.text())
        # Call the sweep_magnetic_field method of the MagnetController
        fields = self.magnet_controller.sweep_magnetic_field(field_range, num_points)
        # Plot the magnetic field vs resistance curve
        self.series1.clear()
        for i in range(num_points):
            self.series1.append(fields[i], 1.0)  # Replace "1.0" with the corresponding resistance value for each point
        # Display the magnetic field range in the GUI
        self.lbl_display_magnetic_field.setText(f"Magnetic Field Range: {field_range} T")



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

    def measure(self):
        # Simulate a current adjustment and receive feedback
        current = np.linspace(0, 1, 100)
        feedback = self.mock_measurement.get_feedback(current)

        # Plot the current vs feedback curve
        self.series.clear()
        for i in range(100):
            self.series.append(current[i], feedback[i])

        # Fit the curve using the fit_curve function from curve_fit.py
        params = fit_curve(np.array([current, feedback]).T)

        # Display the fitted parameters in the GUI
        self.lbl_display.setText(f"Fitted Parameters: {params}")


if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    #


