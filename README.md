# DC Magnetoresistance and Hall Effect Measurement GUI

This Python GUI is designed to perform DC magnetoresistance and Hall effect measurements using various instruments including LakeShore temperature controller, Keithley current source, and IPS120 magnet power supply. It also includes features for curve fitting and data conversion.

# Getting Started
# Prerequisites
This software requires the following Python packages to be installed:

```
PyQt5
```

```
PyVISA
```
# Installation
Clone this repository to your local machine
Install the required Python packages using pip:
```
pip install pyqt5 pyvisa
```
# Running the Program
To run the program, navigate to the repository directory and execute the following command:
```
python main.py
```

#Installation
# Clone the repository: 

```
git clone git@github.com:TeinkBR/PI_1_measurment_py.git
```
# Install PyVISA: 
```
pip install pyvisa
```
# Install PyQt5: 
```python
pip install pyqt5
```
# Run the main file: 
```python
python main.py
```
# Usage

Connect the LakeShore 336 temperature controller, Keithley 2400 sourcemeter, and IPS 120-10 power supply to the computer via GPIB.
Run the software by executing the 'main.py file'.
Set the temperature setpoint, current setpoint, and magnetic field setpoint in the corresponding text boxes.
Click the `"Measure Temperature", `"Measure Current", and `"Set Magnetic Field" buttons to take measurements and control the magnetic field.
Click the "Curve Fitting" button to fit the data to a curve.
Click the "Convert Data" button to convert the data to an origin-readable file format.

License
This software is licensed under the MIT License. See the LICENSE file for details.



