#!./py_env/bin/python

import rpi_ws281x as ws281x
from time import sleep

led_count = 150

led_strip=ws281x.PixelStrip(num=led_count, pin=21, freq_hz=800000)
led_strip.begin()

# pix.getBrightness()     pix.getPixelColor(      pix.getPixelColorRGB(   pix.getPixelColorRGBW(  pix.getPixels()
# pix.getPixels()
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

led_strip.setBrightness(160)
while True:
    for phase in range(0, led_count):
        for num in range(0, led_count):
            bright=num+phase
            bright%=(led_count//4)
            bright*=255
            bright//=led_count//4
            led_strip.setPixelColorRGB(num,bright,0,bright)
        led_strip.show()
        sleep(0.01)
        # led_strip.setPixelColorRGB(num,0,0,0)
        # print("Ph", phase)

sleep(30)
led_strip.setBrightness(0)
led_strip.show()
