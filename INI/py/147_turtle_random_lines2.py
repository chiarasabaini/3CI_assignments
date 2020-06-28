__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2020/01/11"

def draw_line(ninja, n):
    """DIsegna linee casuali, di diverse dimensioni e colori
    """

    import turtle
    import random

    t = turtle.Turtle()
    r = random.Random()

    t.colormode(255, 255, 255)
    
    for _ in range(n):
        t.down()
        t.width(r.randint(1, 9))
        r = r.randint(0, 255)
        g = r.randint(0, 255)
        b = r.randint(0, 255)
        t.color(r, g, b)
        xpos = r.randint(0, 300)
        ypos = r.randint(0, 400)
        t.goto(xpos, ypos)
        t.forward(r.randint(20, 420))

