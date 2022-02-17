import opc
import time
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


for led in range (24, 31):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range (31, 300,60):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range (144, 151):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)    
for led in range (264, 272):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range (0, 360):
    leds[led] = (0,0,0)
    client.put_pixels(leds)    

for led in range (24, 31):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range (31, 92,60):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)  
for led in range (144, 152):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range (204, 265,60):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range (265,273):
    leds[led] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for led in range (0, 360):
    leds[led] = (0,0,0)
    client.put_pixels(leds) 

for led in range (31,360,60):
    leds[led] = (255,0,0)
    time.sleep(0.5)
    client.put_pixels(leds)    
for led in range (0, 360):
    leds[led] = (0,0,0)
    client.put_pixels(leds)
    
for led in range (24, 31):
    leds[led] = (255,0,0)
    time.sleep(0.05)
    client.put_pixels(leds)
for led in range (31,300,60):
    leds[led] = (255,0,0)
    time.sleep(0.05)
    client.put_pixels(leds)
for led in range (264, 271):
    leds[led] = (255,0,0)
    time.sleep(0.05)
    client.put_pixels(leds)
for led in range (24,300,60):
    leds[led] = (255,0,0)
    time.sleep(0.05)
    client.put_pixels(leds)
for led in range (0, 360):
    leds[led] = (0,0,0)
    client.put_pixels(leds)     

