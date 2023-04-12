

import pyvisa as visa

class Keithley2612BController:
    def __init__(self, ip_address):
        self.keithley = visa.ResourceManager().open_resource(f"TCPIP0::{ip_address}::5025::SOCKET")
        
    def reset(self):
        self.keithley.write("smua.reset()")
        
    def set_source_function(self, function):
        self.keithley.write(f"smua.source.func=smua.{function}")
        
    def set_source_voltage(self, voltage):
        self.keithley.write(f"smua.source.levelv={voltage}")
        
    def set_source_voltage_range(self, voltage_range):
        self.keithley.write(f"smua.source.rangev={voltage_range}")
        
    def set_source_current_limit(self, current_limit):
        self.keithley.write(f"smua.source.limiti={current_limit}")
        
    def set_measurement_current_range(self, current_range):
        self.keithley.write(f"smua.measure.rangei={current_range}")
        
    def enable_source_output(self):
        self.keithley.write("smua.source.output=smua.OUTPUT_ON")
        
    def disable_source_output(self):
        self.keithley.write("smua.source.output=smua.OUTPUT_OFF")
        
    def measure_current(self):
        return self.keithley.ask("smua.measure.i()")


# In[7]:


k2612B = Keithley2612BController("169.254.000.001")
k2612B.reset()
k2612B.set_source_function("OUTPUT_DCVOLTS")
k2612B.set_source_voltage_range(20)
k2612B.set_source_voltage(5)
k2612B.set_source_current_limit(10e-3)
k2612B.set_measurement_current_range(10e-3)
k2612B.enable_source_output()
current = k2612B.measure_current()
k2612B.disable_source_output()
k2612B.reset()


# In[ ]:




