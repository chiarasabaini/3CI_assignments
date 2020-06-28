'''Programma che tramite turtle stampa a video i gradini
@author Sabaini Chiara 3CI
@version 0.1 2019/12/dd
'''
import turtle

n = int(input("Quanti gradini? "))
h = int(input("Altezza? "))
l = int(input("Larghezza? "))
a = 90
def rotate_dx(t, a):
    t.right(a)

def rotate_sx(t, a):
    t.left(a)

def go(t, h):
    t.forward(h)


t = turtle.Turtle()

t.width(5)
t.color("purple")
t.down()

for _ in range(n):
    rotate_sx(t, 90)
    go(t, h)
    rotate_dx(t, 90)
    go(t, l)
