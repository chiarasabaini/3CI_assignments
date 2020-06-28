__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2019/12/16"

def draw_polygon(n, side, color):
    """
    Disegna un poligono di n lati con una data dimensione per il lato
    """
    import turtle
    t = turtle.Turtle()
    
    t.color(color)
    amp = 360 / n
    t.width(5)
    t.clear()
    t.shape("turtle")
    
    for _ in range(n):
        t.forward(side)
        t.left(amp)
        
        
