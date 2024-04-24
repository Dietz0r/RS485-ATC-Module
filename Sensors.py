from Settings import SensorPins
import lib.umodbus.modbus as modbus
import asyncio
import time

def SensorSetup():
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
        
        # set up pin change interrupt functions
        for i in range(SensorPins.SensorNum):
            SensorPins.Sensor[i+1].irq(trigger = SensorPins.Sensor[i+1].IRQ_HIGH_LEVEL | SensorPins.Sensor[i+1].IRQ_LOW_LEVEL, handler=set_register)

def set_register(Pin):
    print(f'Input pin level change: Pin{Pin}')