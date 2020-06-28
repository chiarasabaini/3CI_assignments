'''
programma che disegna un rettangolo n x m in ASCII art
@author Sabaini Chiara 3CI
@version 0.1 2019/12/dd
'''
n = int(input("Righe? "))
m = int(input("Colonne? "))
char = "#"
space = " "

for i in range(1, n + 1, 1):
    print((char + space) * m)