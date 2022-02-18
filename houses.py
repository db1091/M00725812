import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(180,360,60):
    leds[120-led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(4,123,59):
    leds[125-led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(4,9):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(69,193,61):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(251,360,60):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(62,69):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(122,130):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(243,304,60):
    leds[187-led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)   
for led in range(244,247):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(247,308,60):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(301,304):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(308,311):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
    
for led in range(135,315,60):
    leds[90-led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(18,137,59):
    leds[154-led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)   
for led in range(19,49):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(109,233,61):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(291,360,60):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(337,352):
    leds[327-led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(264,270):
    leds[180-led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(309,325):
    leds[280-led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(77,110):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)
for led in range(137,171):
    leds[led] = (255,0,0)
    time.sleep(.01)
    client.put_pixels(leds)     
