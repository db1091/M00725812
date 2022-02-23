import opc
import time

leds = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
print(leds)
while True: #ask questions infinitely after every animation 
    print("Which animation would you like to display?")
    print("a. Benjo's custom flag")
    print("b. Rainfall")
    print("c. countdown")
    print("d. houses")
    print("e. traffic light")
    print("f. primary colours making secondary colours")
    x = input() #x equals to any reply given

    if x == "a":
        for led in range(60): #pick out indeces: led = 0,1,2,3...60
            leds[led] = (255,0,0) #red leds
            time.sleep(.01)#delay the frame a bit
            client.put_pixels(leds)#print pixels
        for led in range(119,360,60): #pick out indeces from 119 to 360 in steps of 60
            leds[led] = (0,255,0) #green leds
            time.sleep(.01)
            client.put_pixels(leds)
        for led in range(300,360):
            leds[299-led] = (0,0,255) #blue leds
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
    elif x == "b":
        leds = [(0,0,0)]*360
        led = 0
        while led<5: #scroll all rows at the same time from 0 to 5
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
        num = 3
        for x in range(num):#do this forever
             for leda in range(183, 360,60):
                  leds[slice(182,187)] = [(0,0,0)]*5 #set specific other indeces as the rain moves
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
    elif x == "c":
        leds = [(0,0,0)]*360 #black before it starts countdown from 3 to 0
        for led in range (24, 31): # 3
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

        for led in range (24, 31): #2
            leds[led] = (255,0,0)
            time.sleep(0.2)
            client.put_pixels(leds)
        for led in range (31, 92,60):
            leds[led] = (255,0,0)
            time.sleep(0.2)
            client.put_pixels(leds)  
        for led in range (144, 152):
            leds[led] = (255,0,0)
            time.sleep(.2)
            client.put_pixels(leds)
        for led in range (204, 265,60):
            leds[led] = (255,0,0)
            time.sleep(0.2)
            client.put_pixels(leds)
        for led in range (265,273):
            leds[led] = (255,0,0)
            time.sleep(0.2)
            client.put_pixels(leds)
        for led in range (0, 360):
            leds[led] = (0,0,0)
            client.put_pixels(leds) 

        for led in range (31,360,60): #1
            leds[led] = (255,0,0)
            time.sleep(0.5)
            client.put_pixels(leds)    
        for led in range (0, 360):
            leds[led] = (0,0,0)
            client.put_pixels(leds)
            
        for led in range (24, 31): #0
            leds[led] = (255,0,0)
            time.sleep(0.2)
            client.put_pixels(leds)
        for led in range (31,300,60):
            leds[led] = (255,0,0)
            time.sleep(0.2)
            client.put_pixels(leds)
        for led in range (264, 271):
            leds[led] = (255,0,0)
            time.sleep(0.2)
            client.put_pixels(leds)
        for led in range (24,300,60):
            leds[led] = (255,0,0)
            time.sleep(0.2)
            client.put_pixels(leds)
        for led in range (0, 360):
            leds[led] = (0,0,0)
            client.put_pixels(leds)     
    elif x == "d": #Houses
        leds = [(0,0,0)]*360    
        for led in range(180,360,60): #small house
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
            
        for led in range(135,315,60): #big house 
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
    elif x == "e": #traffic light
        leds = [(0,0,0)]*360 
        for led in range(64,264,60): #red traffic light
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
            

        for led in range(81,264,60): #yellow traffic light
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
            
        for led in range(98,300,60): #green traffic light
            leds[led] = (0,255,0)
            leds[led+1] = (0,255,0)
            time.sleep(0.1)
            client.put_pixels(leds)
        for led in range(156,162):
            leds[led] = (0,255,0)
            leds[led+60] = (0,255,0)
            time.sleep(0.1)
            client.put_pixels(leds)
    elif x == "f":
        leds = [(0,0,0)]*360 
        led = 0
        while led<30: #scroll all rows at the same time
         for rows in range(3): #first three rows left to right
             leds[led + rows*60] = (255,0,0)
         for rows in range(3): #last three rows reversed (right to left)
             leds[59-led + rows*60] = (255,255,0)
         client.put_pixels(leds)
         time.sleep(.1)
         led = led + 1
        led = 30
        while led<60: #scroll all rows at the same time
         for rows in range(3): #first three rows left to right
             leds[led + rows*60] = (255,165,0)
         for rows in range(3): #last three rows reversed (right to left)
             leds[59-led + rows*60] = (255,165,0)
         client.put_pixels(leds)
         time.sleep(.1)
         led = led + 1
        led = 180
        while led<210: #scroll all rows at the same time
         for rows in range(3): #first three rows left to right
             leds[led + rows*60] = (0,0,255)
         for rows in range(3): #last three rows reversed (right to left)
             leds[59-led + rows*60] = (255,0,0)
         client.put_pixels(leds)
         time.sleep(.1)
         led = led + 1
        led = 210
        while led<240: #scroll all rows at the same time
         for rows in range(3): #first three rows left to right
             leds[led + rows*60] = (143,0,255)
         for rows in range(3): #last three rows reversed (right to left)
             leds[59-led + rows*60] = (143,0,255)
         client.put_pixels(leds)
         time.sleep(.1)
         led = led + 1
        led = 0
        while led<30: #scroll all rows at the same time
         for rows in range(6): #first three rows left to right
             leds[led + rows*60] = (0,0,255)
         for rows in range(6): #last three rows reversed (right to left)
             leds[59-led + rows*60] = (255,255,0)
         client.put_pixels(leds)
         time.sleep(.1)
         led = led + 1
        led = 30
        while led<60: #scroll all rows at the same time
         for rows in range(6): #first three rows left to right
             leds[led + rows*60] = (0,255,0)
         for rows in range(6): #last three rows reversed (right to left)
             leds[59-led + rows*60] = (0,255,0)
         client.put_pixels(leds)
         time.sleep(.1)
         led = led + 1 
            
    else:
        print("That is not a valid input.") # any other reply apart from the options
            

                 

