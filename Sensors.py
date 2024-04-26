from machine import Pin
from Settings import SensorPins
from client import client

SensorPins = SensorPins()

## SensorSetup
# set up weak internal pull_up or pull_down resistors
if SensorPins.PullUpDown == 'Up':
    for i in range(SensorPins.SensorNum):
        SensorPins.Sensor[i].init(pull = SensorPins.Sensor[7].PULL_UP)
    print(f'Setting Sensorpins to internal Pull_Up mode')
elif SensorPins.PullUpDown == 'Down':
    for i in range(SensorPins.SensorNum):
        SensorPins.Sensor[i].init(pull = SensorPins.Sensor[7].PULL_DOWN)
    print(f'Setting Sensorpins to internal Pull_Down mode')
else:
    print(f'Leaving SensorPins in default state.')

class SensorFunctions():
    def Update(self,reg_type: any, address: int, val: list[bool]):
        """Update the discrete input registers for the sensorpins via callback.
        Args:
            address (int): The sensor pin to update.
            val (list[bool]): Current state of the Register.  Only the first value of the array is used, the rest are ignored.
        """
        global client
        
        if bool(SensorPins.Sensor[address-257].value()) == val[0]:      #arrays start counting at 0, you numpty!
            print(f'Sensorpin {address-256}: no change')
        else:
            val[0] = not val[0]
            client.set_ist(address, val)
            print(f'Updated SensorPin {address} to state: {val}')
