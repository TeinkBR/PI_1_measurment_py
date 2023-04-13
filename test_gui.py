import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QSlider, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up voltage knob
        voltage_group_box = QGroupBox("Voltage")
        voltage_slider = QSlider(Qt.Horizontal, voltage_group_box)
        voltage_slider.setMaximum(100)
        voltage_slider.setValue(50)

        # Set up current knob
        current_group_box = QGroupBox("Current")
        current_slider = QSlider(Qt.Horizontal, current_group_box)
        current_slider.setMaximum(100)
        current_slider.setValue(50)

        # Set up magnetic field knob
        magnetic_field_group_box = QGroupBox("Magnetic Field")
        magnetic_field_slider = QSlider(Qt.Horizontal, magnetic_field_group_box)
        magnetic_field_slider.setMaximum(100)
        magnetic_field_slider.setValue(50)

        # Set up temperature knob
        temperature_group_box = QGroupBox("Temperature")
        temperature_slider = QSlider(Qt.Horizontal, temperature_group_box)
        temperature_slider.setMaximum(100)
        temperature_slider.setValue(50)

        # Set up layout for knobs
        knob_layout = QVBoxLayout()
        knob_layout.addWidget(voltage_group_box)
        knob_layout.addWidget(current_group_box)
        knob_layout.addWidget(magnetic_field_group_box)
        knob_layout.addWidget(temperature_group_box)

        # Set up plot for resistance vs. time
        resistance_fig = Figure()
        resistance_canvas = FigureCanvas(resistance_fig)
        resistance_ax = resistance_fig.add_subplot(111)
        resistance_ax.set_xlabel("Time (s)")
        resistance_ax.set_ylabel("Resistance (ohms)")

        # Set up layout for window
        layout = QHBoxLayout()
        layout.addLayout(knob_layout)
        layout.addWidget(resistance_canvas)

        # Set up central widget for window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set up function for calculating resistance
        def calculate_resistance(voltage, current):
            return voltage / current

        # Set up legend for plot
        resistance_ax.legend()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
