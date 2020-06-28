'''
programma che disegna un rettangolo n x m in ASCII art
@author Sabaini Chiara 3CI
@version 0.1 2019/12/dd
'''
n = int(input("Righe? "))
m = int(input("Colonne? "))
char = "#"
space = " "

while n > 0:
    print((char + space) * m)
    n -= 1