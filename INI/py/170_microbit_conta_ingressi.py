@author = "Sabaini Chiara 3CI"
@version = "1.0 2020-01-16"

from microbit import *

cont = 0

if button_a.get_presses() && button_b.get_presses():
    display.scroll(cont)
    
else:   
    elif button_a.get_presses():
        cont += 1
    
    elif button_b.get_presses():
        cont -=1
