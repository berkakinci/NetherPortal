#!./py_env/bin/python

import rpi_ws281x as ws281x

led_count = 150

led_strip=ws281x.PixelStrip(num=led_count, pin=21, freq_hz=800000)
led_strip.begin()
led_strip.show()
