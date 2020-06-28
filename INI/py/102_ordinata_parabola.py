'''
programma che calcola l'ordinata di una parabola i cui valori dei coefficienti e
dell'ascissa vengono forniti dall'utente
@author Sabaini Chiara 3CI
@version 1.0 2019/11/18
'''

a = eval(input("inserisci a: "))
b = eval(input("inserisci b: "))
c = eval(input("inserisci c: "))
x = eval(input("inserisci x: "))

y = a*(x**2) + b*x + c

print("y = ", y)
