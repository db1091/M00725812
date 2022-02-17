import opc
import time
import random

leds = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(64,264,60):
    leds[led] = (255,0,0)
    leds[led+1] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range(122,129):
    leds[led] = (255,0,0)
    leds[led+60] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range (0, 360):
    leds[led] = (0,0,0)
    client.put_pixels(leds)    
    

for led in range(81,264,60):
    leds[led] = (255,255,0)
    leds[led+1] = (255,255,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range(139,146):
    leds[led] = (255,255,0)
    leds[led+60] = (255,255,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range (0, 360):
    leds[led] = (0,0,0)
    client.put_pixels(leds)
    
for led in range(98,300,60):
    leds[led] = (0,255,0)
    leds[led+1] = (0,255,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range(156,162):
    leds[led] = (0,255,0)
    leds[led+60] = (0,255,0)
    time.sleep(0.1)
    client.put_pixels(leds)   
    
    
