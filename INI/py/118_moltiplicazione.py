'''Programma che calcola il prodotto di due numeri positivi forniti in input dall'utente
@author Sabaini Chiara 3CI
@version 0.1 2019/12/02
'''
n = int(input("Inserisci moltiplicando: "))
m = int(input("Inserisci moltiplicatore: "))
prod = 0

for i in range(0, m, 1):
    prod = prod + n

print("Il prodotto tra {} e {} è {}".format(n, m, prod))