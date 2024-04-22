from neopixel import NeoPixel
from Settings import ARGB

ARGB = Settings.ARGB()

RGB  = NeoPixel(ARGB.RGBpin, ARGB.NumLeds)

# set RGB coded solid color
def setRGBsolid(r, g, b):
    for i in range(ARGB.NumLeds):
        RGB[i] = (r, g, b)
    RGB.write()