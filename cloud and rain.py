import opc
import time
import random

leds = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 0
while led<5: #scroll all rows at the same time
    leds[led+2] = (255,255,255) # set the leds to colour white, incrementing position each frame
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
while True:  #do this forever
     for leda in range(183, 360,60):
          leds[slice(182,187)] = [(0,0,0)]*5 #set specific indeces to black
          leds[slice(242,247)] = [(0,0,0)]*5
          leds[slice(302,307)] = [(0,0,0)]*5
          leds[leda] = (0,0,255)
          leds[leda+1] = (0,0,255)
          leds[leda+3] = (0,0,255)
          if leda == 303: # if rain drops reach 303 
                leda = 183 # a new rain fall starts from 183
          client.put_pixels(leds)
          time.sleep(0.5)#rainfall speed
   for leda in range(192, 360,60):
          leds[slice(192,197)] = [(0,0,0)]*5
          leds[slice(251,256)] = [(0,0,0)]*5
          leds[slice(311,316)] = [(0,0,0)]*5
          leds[leda] = (0,0,255)
          leds[leda+1] = (0,0,255)
          leds[leda+3] = (0,0,255)
          if leda == 303:
                leda = 192
          client.put_pixels(leds)
          time.sleep(0.5)

    
     for leda in range(200, 360,60):
          leds[slice(200,205)] = [(0,0,0)]*5
          leds[slice(259,264)] = [(0,0,0)]*5
          leds[slice(320,325)] = [(0,0,0)]*5
          leds[leda] = (0,0,255)
          leds[leda+1] = (0,0,255)
          leds[leda+3] = (0,0,255)
          if leda == 320:
                leda = 200
          client.put_pixels(leds)
          time.sleep(0.5)
       
     for leda in range(208, 360,60):
          leds[slice(208,213)] = [(0,0,0)]*5
          leds[slice(268,273)] = [(0,0,0)]*5
          leds[slice(328,333)] = [(0,0,0)]*5
          leds[leda] = (0,0,255)
          leds[leda+1] = (0,0,255)
          leds[leda+3] = (0,0,255)
          if leda == 328:
                leda = 208
          client.put_pixels(leds)
          time.sleep(0.5)   
