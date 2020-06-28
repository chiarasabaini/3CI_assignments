__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-01-16"

import turtle
import time

t = turtle.Turtle()

def square(sprite, side, pen_color="black", pen_size=1, shape="ninja.gif"):
    """Disegna, muovendo l'oggetto di tipo Turtle sprite,
    un quadrato di dimensione size con un certo colore e dimensione della penna,
    dopo il disegno di un lato attende mezzo secondo time.sleep(0.5)
    """

    for _ in range(4):
        t.forward(side)
        t.left(90)

    time.sleep(0.5)
        
if __name__ == "__main__":
    square(shape, 100)
