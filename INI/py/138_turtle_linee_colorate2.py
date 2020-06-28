__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2019/12/23"

def draw_line(ninja, n, l, d, dim, color):
    """La Turtle <ninja> sposta in alto di <d> e
    disegna <n> linee lunghe <l> di dimensione <dim> e colore <color>
    """

    import turtle
    import random

    t = turtle.Turtle()

    t.width(dim)
    t.color(color)
    t.shape(ninja)
    
    for _ in range(n):
        t.up()
        t.left(90)
        t.forward(d)
        t.left(90)
        t.forward(l)
        t.right(180)
        t.down()
        t.forward(l)
