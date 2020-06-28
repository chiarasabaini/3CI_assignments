@author = "Sabaini Chiara 3CI"
@version = "1.0 2020-01-16"

from microbit import *

xpos = 0
ypos = 0

while True:
    led.plot(xpos, ypos)
    
    x = accelerometer.get_x()
    
    if x > 20:
        xpos += 1
    elif reading < -20:
        xpos -= 1
    
    y = accelerometer.get_y()
    
    if y > 20:
        ypos += 1
    elif reading < -20:
        ypos -= 1