__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-01-17"

import turtle
import random

def draw_polygon(t, n_sides, size, color):
    """Disegna un poligono colorato
    """
    t.width(3)
    t.color(color)
    alfa = 360 / n_sides
    
    for _ in range(n_sides):
        t.forward(size)
        t.left(alfa)
    
    
def draw_polygons(n, size):
    """Disegna una serie di poligoni colorati concentrici
    """
    t = turtle.Turtle()
    r = random.Random()

    colors = "red", "yellow", "blue", "lightblue", "green", "pink", "purple", "black", "fuchsia"

    for i in range(3, n + 3):
        color = r.choice(colors)
        draw_polygon(t, i, size, color)

if __name__ == "__main__":
    draw_polygons(7, 100)
