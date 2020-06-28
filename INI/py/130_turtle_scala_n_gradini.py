'''Programma che tramite turtle stampa a video i gradini
@author Sabaini Chiara 3CI
@version 0.1 2019/12/dd
'''
from turtle import *

n = int(input("Quanti gradini? "))
h = int(input("Altezza? "))
l = int(input("Larghezza? "))

width(5)
color("purple")
down()

for _ in range(n):
    left(90)
    forward(h)
    right(90)
    forward(l)
