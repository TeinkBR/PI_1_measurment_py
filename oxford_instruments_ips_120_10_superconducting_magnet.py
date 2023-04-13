from time import sleep
from typing import List, Tuple
from Lakeshore_336_Temperature_controller import LakeShoreController
from Keithley2182_nanovoltmeter import KeithleyController
from Keithley_2612_B_System_source_meter import IPS120Controller
from oxford_ips_120_10_superconducting_magnet import IPS120_10


class MagnetController:
    def __init__(self):
        # Create instances of the subprogram classes
        self.lakeshore = LakeShoreController("GPIB::1")
        self.keithley = KeithleyController("GPIB::12")
        self.ips = IPS120Controller("GPIB::25")
        self.magnet = IPS120_10("GPIB::25")  # Default channel for the IPS

    def ramp_up_magnetic_field(self, field_setpoint: float) -> None:
        """Ramp up the magnetic field to the specified setpoint."""
        self.ips.enable_control()  # Enables the power supply and remote control
        self.magnet.train_magnet([
            (11.8, 1.0),
            (13.9, 0.4),
            (14.9, 0.2),
            (16.0, 0.1),
        ])
        self.magnet.set_field(field_setpoint)  # Bring the magnet to the setpoint
        while abs(self.magnet.field - field_setpoint) > 0.1:  # Wait until the magnet reaches the setpoint
            sleep(1)
        self.ips.disable_control()  # Disables the control of the supply, turns off the switch-heater and clamps the output.

    def sweep_magnetic_field(self, field_range: Tuple[float, float], num_points: int) -> List[float]:
        """Sweep the magnetic field over the specified range and return the field values."""
        start, stop = field_range
        step = (stop - start) / (num_points - 1)
        fields = []
        for i in range(num_points):
            field_setpoint = start + i * step
            self.ramp_up_magnetic_field(field_setpoint)
            field = self.read_magnetic_field()
            fields.append(field)
        return fields

    def read_magnetic_field(self) -> float:
        """Read the magnetic field and return its value."""
        return self.magnet.field


if __name__ == "__main__":
    magnet_controller = MagnetController()

    # Set a point for the magnetic field strength
    magnet_controller.ramp_up_magnetic_field(10)  # Bring the magnet to 10 T
    field = magnet_controller.read_magnetic_field()  # Read the magnetic field
    print(f"Magnetic field: {field} T")

    # Sweep the magnetic field over a range of values
    field_range = (8, 12)  # T
    num_points = 21
    fields = magnet_controller.sweep_magnetic_field(field_range, num_points)
    print(f"Magnetic field values: {fields}")
