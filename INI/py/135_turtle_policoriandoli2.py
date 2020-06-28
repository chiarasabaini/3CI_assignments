__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2019/12/22"

def policoriandoli2(w, h):
    """Draw continuosly colored circle,
    in a window w x h.
    """
    import random
    import turtle

    t = turtle.Turtle()
    wn = turtle.Screen()
    
    t.speed(10)
    i = random.randint(1, 500)
    w, h = 800, 600
    wn.setup(w, h)
    turtle.colormode(255)
    t.shape("circle")
    t.hideturtle()

    for _ in range(i):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.fillcolor(r, g, b)
        t.color(r, g, b)
        t.stamp()
        t.forward(random.randint(5, 300))
        t.right(random.randint(0, 350))
