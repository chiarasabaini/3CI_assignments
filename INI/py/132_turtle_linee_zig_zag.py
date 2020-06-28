'''
<descrizione programma>
@author Sabaini Chiara 3CI
@version 0.1 2019/12/dd
'''
import random
from turtle import *

i = random.randint(1, 500)
w, h = 800, 600
setup(w, h)
colormode(255)
width(3)
for _ in range(i):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color(r, g, b)
    forward(random.randint(5, 300))
    right(random.randint(0, 350))

