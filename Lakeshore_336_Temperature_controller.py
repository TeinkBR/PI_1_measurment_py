


import pymeasure
from pymeasure.instruments.lakeshore import LakeShore336

classpymeasure.instruments.lakeshore.lakeshore_base.LakeShoreTemperatureChannel(parent, id)
class LakeshoreController:
    def __init__(self, gpib_address):
        self.controller = LakeShore336(gpib_address)
        
    def set_setpoint(self, loop_number, setpoint):
        getattr(self.controller, f"loop{loop_number}").setpoint = setpoint
        
    def set_heater_range(self, loop_number, heater_range):
        getattr(self.controller, f"loop{loop_number}").heater_range = heater_range
        
    def wait_for_temperature(self, sensor_letter):
        getattr(self.controller, f"input_{sensor_letter}").wait_for_temperature()
        
    def get_temperature(self, sensor_letter):
        return getattr(self.controller, f"input_{sensor_letter}").temperature
        
    def plot_temperature(self, sensor_letter):
        data = []
        for i in range(50):
            data.append(self.get_temperature(sensor_letter))
            pylab.plot(data)
            pylab.xlabel('Time (s)')
            pylab.ylabel('Temperature (K)')
            pylab.title('Temperature Sensor {} vs. Time'.format(sensor_letter))
            pylab.grid(True)
            pylab.show()


# In[ ]:


controller = LakeshoreController("GPIB::1")

controller.set_setpoint(1, 50)
controller.set_heater_range(1, 'low')
controller.wait_for_temperature('A')
temperature_A = controller.get_temperature('A')
print(temperature_A)

controller.plot_temperature('A')

