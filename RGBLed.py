from neopixel import NeoPixel
import Settings

ARGB = Settings.ARGB()

RGB  = NeoPixel(ARGB.RGBpin, ARGB.NumLeds)

# set RGB coded solid color
def setRGBsolid(g, r, b):
    for i in range(ARGB.NumLeds):
        RGB[i] = (g, r, b)
    RGB.write()