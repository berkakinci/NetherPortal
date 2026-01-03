#!./py_env/bin/python

import rpi_ws281x as ws281x
import numpy
from time import sleep

led_count = 150


#leds.begin()             leds.getPixelColorRGBW(  leds.setGamma(           leds.size
#leds.getBrightness()     leds.getPixels()         leds.setPixelColor(
#leds.getPixelColor(      leds.numPixels()         leds.setPixelColorRGB(
#leds.getPixelColorRGB(   leds.setBrightness(      leds.show()

class LEDStrip(ws281x.PixelStrip):
    class Pixel:
        def __init__(self, r=0, g=0, b=0):
            self.r = r
            self.g = g
            self.b = b

        def multiply(self, factor):
            self.r *= factor
            self.g *= factor
            self.b *= factor

    class Image:
        def __init__(self, x, y):
            "Image that we will use to imply with the strips along the edge."
            x+=2 # Displace side LEDs left and right
            y+=1 # Displate top LEDs up
            self.pixels=numpy.ones((y, x, 3), dtype=numpy.float64)

        def getROI(self):
            "Gets edge LEDs in order of strip Left, Top, Right"
            pixlist=[self.pixels[-1:0:-1,0],
                     self.pixels[0,1:-1],
                     self.pixels[1:,-1]]
            print(pixlist[0].shape, pixlist[1].shape, pixlist[2].shape)
            pixlist=numpy.concatenate(pixlist)
            return pixlist

    def __init__(self, num, max_current=2.0, pin=21, freq_hz=800000, **kwargs):
        # Set up the LED strip
        super().__init__(num=num, pin=pin, freq_hz=freq_hz, **kwargs)
        self.max_current=max_current
        # Set up the image we will try to imply
        x=26 # LEDs across top
        y=(num-x)//2 # LEDs on each side
        print(num, ' -> ', x, y, x+2*y)
        self.image=LEDStrip.Image(x,y)
        self.begin()

    def multiply(self, factor=0.5):
        self.image *= factor

    def totalCurrent(self):
        ledFullCurrent=20e-3 # A
        currents=ledFullCurrent * self.image.getROI()
        print(currents.shape, currents)
        return numpy.sum(currents)

    def isOverCurrent(self):
        current=self.totalCurrent()
        print(current)
        return(current > self.max_current)

    def show(self):
        if self.isOverCurrent():
            raise ValueError("LED Strip OverCurrent")
        super().show()

leds=LEDStrip(num=led_count)

leds.setBrightness(255)
for num in range(0, led_count):
    leds.setPixelColorRGB(num,255,0,255)
    leds.show()
    sleep(0.01)
    leds.setPixelColorRGB(num,0,0,0)


leds.setBrightness(0)
leds.show()
