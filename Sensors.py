from Settings import SensorPins
import lib.umodbus.modbus as modbus
import _thread
import time

def SensorControl():
    def __init__(self):
        if SensorPins.PullUpDown == "Up":
            for i in range(SensorPins.SensorNum):
                SensorPins.Sensor[i].init(SensorPins.Sensor[i].PULL_UP)
                print(f'Setting Sensorpins to internal Pull_Up mode')
        elif SensorPins.PullUpDown == "Down":
            for i in range(SensorPins.SensorNum):
                SensorPins.Sensor[i].init(SensorPins.Sensor[i].PULL_DOWN)
                print(f'Setting Sensorpins to internal Pull_Down mode')
        else:
            print(f'Leaving SensorPins in default state.')

delay = (SensorPins.Timing / 1000)    # delay in ms

def sensor_thread(delay, id):
    while True:
        time.sleep(delay)
        print(f'Running sensor thread {id} every {delay}ms')

_thread.start_new_thread(sensor_thread, (delay, 1))