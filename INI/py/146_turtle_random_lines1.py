'''
<descrizione programma>
@author Sabaini Chiara 3CI
@version 0.1 2019/12/dd
'''
import random
from turtle import *

i = random.randint(1, 500)
w, h = 400, 300
colors = ["red", "blue", "green", "pink", "black", "orange", "yellow", "brown"]

speed(0)
setup(w, h)
width(3)
k = 0
if xpos < h:
    xpos = 0
for _ in range(i):
    color(colors[k])
    forward(random.randint(5, 300))
    right(random.randint(0, 350))
    up()
    forward(random.randint(5, 300))
    down()
    k += 1
    if k == 8:
        k = 0
