from neopixel import NeoPixel
import Settings
import time

ARGB = Settings.ARGB()

RGB  = NeoPixel(ARGB.RGBpin, ARGB.NumLeds)

# set RGB coded solid color
def setRGBsolid(g, r, b):
    for i in range(ARGB.NumLeds):
        RGB[i] = (g, r, b)
    RGB.write()

# blink RGB coded solid color
def setRGBblink(g,r,b, blinks):
    if blinks == 'forever':  
        while True:
            try:
                for i in range(ARGB.NumLeds):
                    RGB[i] = (g, r, b)
                RGB.write()
                time.sleep(0.5)
                for i in range(ARGB.NumLeds):
                    RGB[i] = (0, 0, 0)
                RGB.write()
                time.sleep(0.5)
            except KeyboardInterrupt:
                print('KeyboardInterrupt, stopping blink...')
                break
    if isinstance(blinks, int):
        for i in range(blinks):
            for i in range(ARGB.NumLeds):
                RGB[i] = (g, r, b)
            RGB.write()
            time.sleep(0.5)
            for i in range(ARGB.NumLeds):
                RGB[i] = (0, 0, 0)
            RGB.write()
            time.sleep(0.5)
    elif not isinstance(blinks, int) and not 'forever':
        print(f'Amount of blinks is not "forever" or integer!')
