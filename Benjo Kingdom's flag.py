import opc
import time
import random

leds = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(60): #pick out indeces: led = 0,1,2,3...60
    leds[led] = (255,0,0) #set leds to red 
    time.sleep(.01) #delay the frame a bit
    client.put_pixels(leds)
for led in range(119,360,60): #pick out indeces: led = 119,179,...360 in steps of 60
    leds[led] = (0,255,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(300,360):
    leds[299-led] = (0,0,255) #move in the reverse direction
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(60,300,60):
    leds[300-led] = (0,255,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(61,119):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(178,240,60):
    leds[led] = (0,255,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(242, 300):    
    leds[180-led] = (0,0,255)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(119,181,60):
    leds[300-led] = (0,255,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(122,178):
    leds[led] = (0,255,0)
    leds[led+60] = (0,255,0)
    time.sleep(.01)
    client.put_pixels(leds)
