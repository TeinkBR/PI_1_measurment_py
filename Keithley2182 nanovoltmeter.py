#!/usr/bin/env python
# coding: utf-8

# This code is used for controlling the KEITHLEY 2182A Nanovoltmeter




import visa

class KeithleyController:
    def __init__(self, gpib_address):
        rm = visa.ResourceManager()
        self.keithley = rm.open_resource(gpib_address)
        
    def reset(self):
        self.keithley.write("*rst; status:preset; *cls")
        
    def set_measurement_interval(self, interval_in_ms):
        self.keithley.write(f"trigger:delay {interval_in_ms / 1000}")
        
    def set_number_of_readings(self, number_of_readings):
        self.keithley.write(f"sample:count {number_of_readings}")
        self.keithley.write("trace:points %d" % number_of_readings)
        
    def enable_measurement(self):
        self.keithley.write("status:measurement:enable 512; *sre 1")
        
    def set_trigger_source(self, source):
        self.keithley.write(f"trigger:source {source}")
        
    def set_trace_feed(self, feed):
        self.keithley.write(f"trace:feed {feed}; feed:control next")
        
    def initiate_measurement(self):
        self.keithley.write("initiate")
        
    def assert_trigger(self):
        self.keithley.assert_trigger()
        
    def wait_for_srq(self):
        self.keithley.wait_for_srq()




keithley = KeithleyController("GPIB::12")
keithley.reset()
keithley.set_measurement_interval(500)
keithley.set_number_of_readings(10)
keithley.enable_measurement()
keithley.set_trigger_source("bus")
keithley.set_trace_feed("sense1")
keithley.initiate_measurement()
keithley.assert_trigger()
keithley.wait_for_srq()

