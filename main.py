## Main.py for RS485 extender board
import RGBLed
RGBLed.setRGBsolid(0, 100, 0)
print('Sensors Setup...')
import Sensors
RGBLed.setRGBsolid(50, 100, 0)
print('Starting RS485...')
import RS485
RGBLed.setRGBsolid(0, 0, 0)
