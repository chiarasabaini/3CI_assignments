__author__ ="Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-23"

import turtle

def draw_quinconce(ninja, n_rows, n_cols, space):
    '''Draws a check board
    '''
    ninja.penup()
    colors =  ["red", "blue"]
    ninja.hideturtle()
    ninja.pensize(3)
    n = 2
    a = 0
    
    for i in range(n_rows):
        for j in range(n_cols):
            if n % 2 == 0:
                ninja.dot(colors[a])
            ninja.fd(space)
            n += 1
        a += 1
        ninja.fd(- space * n_cols)
        ninja.left(90)
        ninja.fd(space)
        ninja.right(90)
        n += 2
        
        if a == 2 :
            a = 0

if __name__ == "__main__":
    ninja = turtle.Turtle()
    draw_quinconce(ninja, n_rows=3, n_cols=5, space=10)