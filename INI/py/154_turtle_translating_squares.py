__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-01-16"

import turtle

t = turtle.Turtle()

def translating_square(side, times=5, distance=10, pen_color="black", pen_size=1):
    """Disegna, muovendo l'oggetto di tipo Turtle sprite, 
    times quadrati di lato size con un certo colore e dimensione della penna 
    e con una distanza distance verticale e orizzontale"""

    for i in range(times):
        for _ in range(4):
            t.forward(side)
            t.left(90)
        t.up()
        t.right(135)
        t.forward(25)
        t.left(135)
        t.down()
    

if __name__ == "__main__":
    translating_square(100)
