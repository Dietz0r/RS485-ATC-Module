from neopixel import NeoPixel
from Settings import misc_pin_settings
import time

argb = misc_pin_settings["argb"]
rgb = NeoPixel(argb["pin"], argb["num_leds"])

num_leds = argb["num_leds"]

# set RGB coded solid color
def setRGBsolid(g, r, b):
    for i in range(num_leds):
        rgb[i] = (g, r, b)
    rgb.write()

# blink RGB coded solid color
def setRGBblink(g, r, b, blinks):
    if blinks == 'forever':  
        while True:
            try:
                for i in range():
                    rgb[i] = (g, r, b)
                rgb.write()
                time.sleep(0.5)
                for i in range(num_leds):
                    rgb[i] = (0, 0, 0)
                rgb.write()
                time.sleep(0.5)
            except KeyboardInterrupt:
                print('KeyboardInterrupt, stopping blink...')
                break
    if isinstance(blinks, int):
        for i in range(blinks):
            for i in range(num_leds):
                rgb[i] = (g, r, b)
            rgb.write()
            time.sleep(0.5)
            for i in range(num_leds):
                rgb[i] = (0, 0, 0)
            rgb.write()
            time.sleep(0.5)
    elif not isinstance(blinks, int) and not 'forever':
        print(f'Amount of blinks is not "forever" or integer!')
