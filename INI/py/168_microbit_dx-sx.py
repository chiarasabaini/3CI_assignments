@author = "Sabaini Chiara 3CI"
@version = "1.0 2020-01-16"

from microbit import *

if button_a.get_presses():
    display.scroll("<")

elif button_b.get_presses():
    display.scroll(">")
