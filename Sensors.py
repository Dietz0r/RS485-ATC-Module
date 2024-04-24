from Settings import SensorPins
import lib.umodbus.modbus as modbus

class SensorHandling():
    def __init__(self):
        # set up weak internal pull_up or pull_down resistors
        if SensorPins.PullUpDown == 'Up':
            for i in range(SensorPins.SensorNum):
                SensorPins.Sensor[i+1].init(SensorPins.Sensor[i+1].PULL_UP)
                print(f'Setting Sensorpins to internal Pull_Up mode')
        elif SensorPins.PullUpDown == 'Down':
            for i in range(SensorPins.SensorNum):
                SensorPins.Sensor[i+1].init(SensorPins.Sensor[i+1].PULL_DOWN)
                print(f'Setting Sensorpins to internal Pull_Down mode')
        else:
            print(f'Leaving SensorPins in default state.')
        
    def Update(self, address: int, val: list[bool]):
        """Update the discrete input registers for the sensorpins via callback.
        Args:
            address (int): The sensor pin to update.
            val (list[bool]): Current state of the Register.  Only the first value of the array is used, the rest are ignored.
        """
        if bool(SensorPins.Sensor[address-256].value()) == val[0]:
            print(f'Sensorpin {address-256}: no change')
        else:
            val = bool(SensorPins.Sensor[address-256].value())
            modbus.set_ist(address, val)
            print(f'Updated SensorPin {address-256} to state: {val}')
            return address, val;