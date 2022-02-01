import opc
import time
import random

leds = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
led = 0
while led<5:
    leds[led+2] = (255,255,255)
    leds[led+11] = (255,255,255)
    leds[led+19] = (255,255,255)
    leds[led+27] = (255,255,255)
    leds[led+122] = (255,255,255)
    leds[led+131] = (255,255,255)
    leds[led+139] = (255,255,255)
    leds[led+147] = (255,255,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
ledz = 61
while ledz<68:
    leds[ledz] = (255,255,255)
    leds[ledz+9] = (255,255,255)
    leds[ledz+17] = (255,255,255)
    leds[ledz+25] = (255,255,255)
    client.put_pixels(leds)
    time.sleep(.1)
    ledz = ledz + 1
while True:
    for leda in range(183, 360,60):
        #leds[183:240] = [(0,0,0)]*360
        leds[leda] = (0,0,255)
        leds[leda+1] = (0,0,255)
        leds[leda+3] = (0,0,255)
        if leda == 303:
            leda = 183
        client.put_pixels(leds)
        time.sleep(2)
while True:
    for ledo in range(242, 360,60):
        #leds[240:300] = [(0,0,0)]*360
        leds[ledo] = (0,0,255)
        leds[ledo+3] = (0,0,255)
        client.put_pixels(leds)
        time.sleep(2)
        
        
