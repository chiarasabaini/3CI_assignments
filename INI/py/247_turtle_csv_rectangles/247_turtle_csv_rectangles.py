__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-05-08"

import turtle

def draw_axes(t, scale):
    """Draws the Cartesian axes"""
    t.color("lightgrey")
    steps = 5
    size = scale * steps
    
    t.penup()
    t.goto(-size, 0)
    t.pendown()

    for step in range(-steps, steps + 1):
        t.write(step, align="Right", font=("Arial", 12, "bold"))
        t.forward(scale)
        
    t.stamp()
    
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.left(90)
 
    for step in range(-steps, steps + 1):
        t.write(step, align="Right", font=("Arial", 12, "bold"))
        t.forward(scale)

    t.stamp()

def draw_rectangles(filename):
    """Draws the borders of the rectangles defined in the specified text file.
    A rectangle is defined by the coordinates of his opposite vertices.
    """
    t = turtle.Turtle()
    scale = 50
    colors = "green", "red", "blue", "orange", "purple", "lightblue"
    index = 0
    
    t.speed(0)
    t.pensize(2)
    draw_axes(t, scale)
    t.pensize(3)
    t.hideturtle()

    for line in open(filename):
        x1, y1, x2, y2 = line.split()
        x1 = int(x1) * scale
        y1 = int(y1) * scale
        x2 = int(x2) * scale
        y2 = int(y2) * scale

        t.penup()
        t.color(colors[index])
        
        t.goto(x1, y1)      
        t.pendown()
        t.goto(x2, y1)
        t.goto(x2, y2)
        t.goto(x1, y2)
        t.goto(x1, y1)
        
        index = (index + 1) % len(colors)
    
    turtle.exitonclick()
        
if __name__ == "__main__":
    filename = "data\\rectangles.txt"
    draw_rectangles(filename)
