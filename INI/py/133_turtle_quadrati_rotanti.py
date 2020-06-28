'''
Draw continuosly rotating squares of a given size
@author Sabaini Chiara 3CI
@version 0.1 2019/12/16
'''
from turtle import *

def rotating_squares(size):
    """Draw continuosly rotating squares of a given size

    >>> rotating_squares(200)
    >>>
    
    >>>rotating_squares(420)
    >>>
    """
    width(3)
    
    for _ in range(36):
        if _ in range(0, 3):
            color("black")
        elif _ in range(3, 7):
            color("yellow")
        elif _ in range(7, 11):
            color("orange")
        elif _ in range(11, 14):
            color("red")
        elif _ in range(11, 14):
            color("pink")
        elif _ in range(14, 18):
            color("purple")
        elif _ in range(18, 22):
            color("blue")
        elif _ in range(22, 26):
            color("green")
        elif _ in range(26, 30):
            color("brown")
        elif _ in range(30, 36):
            color("grey")
            
        for j in range(4):
            forward(size)
            left(90)
        left(10)
