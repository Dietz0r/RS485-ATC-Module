from machine import Pin
from Settings import sensor_pin_settings
from client import client


class SensorFunctions():
    
    def __init__(self, pins):
        self.sensors = self.build_sensors(pins)
        
    def build_sensors(self, pins) -> tuple[Pin]:
        if "pull_up_or_down" in sensor_pin_settings:
            pull_up_down = sensor_pin_settings["pull_up_or_down"]
            sensors = tuple(Pin(i, Pin.IN, pull_up_down) for i in pins)
        else:
            sensors = tuple(Pin(i, Pin.IN) for i in pins)
        return sensors
    
    def update(self, reg_type: any, address: int, val: list[bool]):
        """Update the discrete input registers for the sensorpins via callback.
        Args:
            address (int): The sensor pin to update.
            val (list[bool]): Current state of the Register.  Only the first value of the array is used, the rest are ignored.
        """
        global client
        
        if bool(self.sensors[address - 257].value()) == val[0]:
            print(f'Sensorpin {address - 256}: no change')
            return
        
        val[0] = not val[0]
        client.set_ist(address, val)
        print(f'Updated SensorPin {address} to state: {val}')


sensor_functions = SensorFunctions(pins=sensor_pin_settings["sensor_pins"])
