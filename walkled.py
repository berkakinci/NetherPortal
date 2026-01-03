#!./py_env/bin/python

import rpi_ws281x as ws281x
from time import sleep

led_count = 150

led_strip=ws281x.PixelStrip(num=led_count, pin=21, freq_hz=800000)
led_strip.begin()

# pix.getBrightness()     pix.getPixelColor(      pix.getPixelColorRGB(   pix.getPixelColorRGBW(  pix.getPixels()
# pix.getPixels()
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

led_strip.setBrightness(255)
for num in range(0, led_count):
    led_strip.setPixelColorRGB(num,255,0,255)
    led_strip.show()
    sleep(0.01)
    led_strip.setPixelColorRGB(num,0,0,0)


led_strip.setBrightness(0)
led_strip.show()
