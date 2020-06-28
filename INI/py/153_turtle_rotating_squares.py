__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-01-16"

import turtle
t = turtle.Turtle()

def rotating_square(side, times, pen_color="black", pen_size=1):
    """Disegna, muovendo l'oggetto di tipo Turtle sprite, times quadrati di lato side 
    con un certo colore e dimensione della penna e con una rotazione degrees gradi"""
    alfa = 360 / times
    for i in range(times):
        for _ in range(4):
            t.forward(side)
            t.left(90)
        t.left(alfa)

if __name__ == "__main__":
    rotating_square(100, 6)
