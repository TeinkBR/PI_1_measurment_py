import pyvisa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time

class NanovoltmeterMeasurement:
    """
    Class to handle measurements using the Keithley 2182 Nanovoltmeter.
    """
    def __init__(self, address='GPIB1::8::INSTR'):
        """
        Initialize the nanovoltmeter object and configure its settings.

        :param address: str, GPIB address of the nanovoltmeter
        """
        self.rm = pyvisa.ResourceManager()
        self.nanovoltmeter = self.rm.open_resource(address)
        self.nanovoltmeter.read_termination = '\n'
        self.nanovoltmeter.write_termination = '\n'
        self.nanovoltmeter.write('SENS:VOLT:DC:NPLC 1')

    def single_measurement(self):
        """
        Perform a single measurement with the nanovoltmeter.

        :return: float, measured voltage in volts
        """
        return float(self.nanovoltmeter.query('READ?'))

    def multiple_measurements(self, N):
        """
        Perform N measurements with the nanovoltmeter.

        :param N: int, number of samples to acquire
        :return: pandas.DataFrame, with columns 't' (time) and 'V' (voltage)
        """
        df = pd.DataFrame(columns=['t', 'V'])
        t0 = time.time()
        for i in range(N):
            df.loc[i] = [time.time()-t0, self.single_measurement()]
        return df

    def plot_results(self, df):
        """
        Plot the results of the measurement in a graph and save it as a PNG file.

        :param df: pandas.DataFrame, with columns 't' (time) and 'V' (voltage)
        """
        fig = plt.figure(figsize=(11.6, 8.2), dpi=300, facecolor='w', edgecolor='k')
        plt.plot(df.t, df.V, 'k.')
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.title('Keithley 2182 Nanovoltmeter measurement (Integration time: 1 PLC @ ' + str(np.round((len(df)-1)/df.iloc[N-1].t, 3)) + ' Sa/s)')
        plt.grid(True)
        plt.savefig('Measurement_result.png')
        plt.show()

if __name__ == '__main__':
    # Initialize the NanovoltmeterMeasurement class
    measurement = NanovoltmeterMeasurement()

    # Perform a single measurement
    print(f"Measured value: {measurement.single_measurement()} Volts.")

    # Perform N measurements
    N = 2048
    df = measurement.multiple_measurements(N)

    # Plot and save the results
    measurement.plot_results(df)
