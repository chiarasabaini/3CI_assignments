"""
Source: collection-comic-speech-bubbles
https://www.freepik.com/free-photos-vectors/label
Label vector created by freepik - www.freepik.com
"""
__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-04-18"

from tkinter import PhotoImage  # Manages PNG not JPG images
from turtle import Turtle, Screen, Shape, setup
from random import randint, choice

def add_shapes(screen, names, shapesize=1):
    for name in names:
        filename = "img/"+ name +".png"
        image = PhotoImage(file=filename).subsample(shapesize)
        screen.addshape(name, Shape("image", image))

def draw_random_image(names, n, w, h):
    """Prints n random img"""
    setup(w, h)
    
    for i in range(n):
        Shape(choice(names))
        x, y = randint(-w//2, w//2), randint(-h//2, h//2)
        turtle.goto(x, y)
        turtle.stamp()
    
if __name__ == "__main__":
    screen = Screen()
    names = ["1", "2", "3", "4", "5", "6"]
    add_shapes(screen, names, shapesize=2)
    draw_random_image(names, 50, w=800, h=600)
    screen.exitonclick()
    
    
