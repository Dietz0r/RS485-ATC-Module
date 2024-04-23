from Settings import Sensors

def SensorControl():
    def __init__(self):
        if Sensor.PullUpDown == "Up":
            for i in range(Sensor.SensorNum):
                Sensors.Sensor[i].init(Sensor.Sensor[i].PULL_UP)
                print(f'Setting Sensorpins to internal Pull_Up mode')
        elif Sensor.PullUpDown == "Down":
            for i in range(Sensor.SensorNum):
                Sensors.Sensor[i].init(Sensor.Sensor[i].PULL_DOWN)
                print(f'Setting Sensorpins to internal Pull_Down mode')
        else:
            print(f'Leaving SensorPins in default state.')