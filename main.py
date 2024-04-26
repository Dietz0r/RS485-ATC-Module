## Main.py for RS485 extender board
import RGBLed
RGBLed.setRGBsolid(0, 100, 0)
print('Sensors Setup...')
import Sensors
RGBLed.setRGBsolid(50, 100, 0)
print('Starting RS485...')
import RS485
print('ModbusClient interruped, flashing warning LED')
RGBLed.setRGBblink(0, 60, 0, 'forever')
