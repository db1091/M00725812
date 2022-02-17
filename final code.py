import opc
import time
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

print("Which animation would you like to display?")
print("a. Benjo's custom flag")
print("b. Rainfall")
print("c. countdown")
print("d. houses")
print("e. traffic light")
x = input()

if x == "a":
    for led in range(60): #pick out indeces: led = 0,1,2,3...
        leds[led] = (255,0,0)
        time.sleep(.01)
        client.put_pixels(leds)
    for led in range(119,360,60):
        leds[led] = (0,255,0)
        time.sleep(.01)
        client.put_pixels(leds)
    for led in range(300,360):
        leds[299-led] = (0,0,255)
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
if x == "b":
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
if x == "c":
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
if x == "d":
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
if x == "e":
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
        time.sleep(0.2)
        client.put_pixels(leds)
    for led in range(139,146):
        leds[led] = (255,255,0)
        leds[led+60] = (255,255,0)
        time.sleep(0.2)
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
        
        

             
