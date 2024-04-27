from machine import Pin, PWM, UART
from typing import Optional, Iterable


class Relay:
    pin_definitions: list[int]
    relays: list[Pin]
    
    def __init__(self, pin_definitions: Optional[Iterable[int]] = None):
        if not pin_definitions:
            pin_definitions = (1, 2, 41, 42, 45, 46)
        self.relays = map(lambda x: Pin(x, Pin.OUT), self.pin_definitions)

    @property
    def channels(self):
        return len(self.pin_definitions)
       
    def get_channel(self, channel: int) -> Optional[Pin]:
        try:
            return self.relays[channel - 1]
        except IndexError:
            return False


rs485_settings = {
    "TX": 17,
    "RX": 18,
    "uart": 1,
    "device_id": 2,
    "baudrate": 19200,
    "bits": 8,
    "parity": None,
    "stop_bit": 1,
}

sensor_pin_settings = {
    "timing": 200,
    "pull_up_or_down": Pin.PULL_UP,
    "sensors_pins": range(3, 11),
}

misc_pin_settings = {
    "dummy_button": {
        "pin": 1,
        "in_out": Pin.IN,
    },
    "argb": {
        "pin": 38,
        "in_out": Pin.OUT,
        "num_leds": 1,
    }
}
