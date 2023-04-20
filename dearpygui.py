import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='DC Magneto-resistance', width=800, height=600)

with dpg.window(label="DC Magneto-resistance"):
    # Add knobs for voltage, current, magnetic field, and temperature ramping
    dpg.add_text("Voltage Ramping")
    dpg.add_slider_float(label="Voltage (V)", default_value=0, max_value=10)
    dpg.add_text("Current Ramping")
    dpg.add_slider_float(label="Current (A)", default_value=0, max_value=5)
    dpg.add_text("Magnetic Field Ramping")
    dpg.add_slider_float(label="Magnetic Field (T)", default_value=0, max_value=2)
    dpg.add_text("Temperature Ramping")
    dpg.add_slider_float(label="Temperature (K)", default_value=0, max_value=300)

    # Add a plot and legend area for resistance
    dpg.add_plot(label="Resistance vs Time")
    dpg.add_legend()
    dpg.add_series(label="Resistance")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()