import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QSlider
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis


class Experiment(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Magnetic Field vs. Resistance Experiment")
        self.setGeometry(100, 100, 1100, 600)

        self.setup_ui()

        self.create_chart()


    def create_chart(self):
        self.chart = QChart()
        self.chart.setTitle("Magnetic Field vs. Resistance")
        self.series = QLineSeries()
        self.chart.addSeries(self.series)

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("Magnetic Field")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("Resistance")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setGeometry(500, 50, 500, 500)
        self.chart_view.setParent(self)

    def setup_ui(self):
        self.btn_start = QPushButton("Start", self)
        self.btn_start.move(50, 50)
        self.btn_start.clicked.connect(self.start_ramp)

        self.btn_pause = QPushButton("Pause", self)
        self.btn_pause.move(50, 100)
        self.btn_pause.clicked.connect(self.pause_ramp)
        self.btn_pause.setEnabled(False)

        self.btn_stop = QPushButton("Stop", self)
        self.btn_stop.move(50, 150)
        self.btn_stop.clicked.connect(self.stop_ramp)
        self.btn_stop.setEnabled(False)

        self.lbl_voltage = QLabel("Voltage Fixed Point:", self)
        self.lbl_voltage.move(200, 50)
        self.txt_voltage = QLineEdit(self)
        self.txt_voltage.move(350, 50)

        self.lbl_magnetic_field = QLabel("Magnetic Field Fixed Point:", self)
        self.lbl_magnetic_field.move(200, 100)
        self.txt_magnetic_field = QLineEdit(self)
        self.txt_magnetic_field.move(350, 100)

        self.lbl_max_magnetic_field = QLabel("Max Magnetic Field:", self)
        self.lbl_max_magnetic_field.move(200, 150)
        self.txt_max_magnetic_field = QLineEdit(self)
        self.txt_max_magnetic_field.move(350, 150)

        self.lbl_magnetic_field_ramp_rate = QLabel("Magnetic Field Ramp Rate:", self)
        self.lbl_magnetic_field_ramp_rate.move(200, 200)
        self.txt_magnetic_field_ramp_rate = QLineEdit(self)
        self.txt_magnetic_field_ramp_rate.move(350, 200)

        self.slider_voltage = QSlider(Qt.Horizontal, self)
        self.slider_voltage.setGeometry(200, 350, 200, 20)
        self.slider_voltage.setMinimum(0)
        self.slider_voltage.setMaximum(100)
        self.slider_voltage.setValue(50)
        self.slider_voltage.valueChanged.connect(self.slider_voltage_changed)

        self.slider_current = QSlider(Qt.Horizontal, self)
        self.slider_current.setGeometry(200, 400, 200, 20)
        self.slider_current.setMinimum(0)
        self.slider_current.setMaximum(100)
        self.slider_current.setValue(50)
        self.slider_current.valueChanged.connect

        self.slider_current.valueChanged.connect(self.slider_current_changed)

        self.slider_magnetic_field = QSlider(Qt.Horizontal, self)
        self.slider_magnetic_field.setGeometry(200, 450, 200, 20)
        self.slider_magnetic_field.setMinimum(0)
        self.slider_magnetic_field.setMaximum(100)
        self.slider_magnetic_field.setValue(50)
        self.slider_magnetic_field.valueChanged.connect(self.slider_magnetic_field_changed)



    def slider_voltage_changed(self, value):
            # TODO: Implement voltage slider functionality
            pass

    def slider_current_changed(self, value):
            # TODO: Implement current slider functionality
            pass

    def slider_magnetic_field_changed(self, value):
            # TODO: Implement magnetic field slider functionality
            pass

    def start_ramp(self):
            # TODO: Implement start ramp function
            self.btn_start.setEnabled(False)
            self.btn_pause.setEnabled(True)
            self.btn_stop.setEnabled(True)

    def pause_ramp(self):
            # TODO: Implement pause ramp function
            self.btn_start.setEnabled(True)
            self.btn_pause.setEnabled(False)
            self.btn_stop.setEnabled(True)

    def stop_ramp(self):
            # TODO: Implement stop ramp function
            self.btn_start.setEnabled(True)
            self.btn_pause.setEnabled(False)
            self.btn_stop.setEnabled(False)

    def run_experiment(self):
            # Open experimental log file
            log_file = open("experimental_log.txt", "w")

            # Begin voltage ramping
            voltage_fixed_point = float(self.txt_voltage.text())
            # TODO: Implement set_voltage function
            # set_voltage(voltage_fixed_point)

            # Begin magnetic field ramping
            magnetic_field = float(self.txt_magnetic_field.text())
            max_magnetic_field = float(self.txt_max_magnetic_field.text())
            magnetic_field_ramp_rate = float(self.txt_magnetic_field_ramp_rate.text())
            while magnetic_field < max_magnetic_field:
                # Set magnetic field
                # TODO: Implement set_magnetic_field function
                # set_magnetic_field(magnetic_field)

                # Record magnetic field to experimental log file
                log_file.write(f'{time.time()}, {magnetic_field}, ')

                # Record current to experimental log file
                # TODO: Implement read_voltage and read_current functions
                # voltage = read_voltage()
                # current = read_current()
                # resistance = voltage / current
                # log_file.write(f'{voltage}, {current}, {resistance}\n')

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Experiment()
        ex.show()
        sys.exit(app.exec_())
