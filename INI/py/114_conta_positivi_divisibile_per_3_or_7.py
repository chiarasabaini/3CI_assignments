'''
programma che, dati in input 10 numeri,
visualizza i numeri maggiori di 0 e divisibili per 3 oppure 7
@author Sabaini Chiara 3CI
@version 0.1 2019/12/02
'''
not0 = 0
div3 = 0
div7 = 0

for i in range(10):
    n = int(input("inserisci numero: "))
    if n > 0:
        not0 = not0 + 1
    if n % 3 == 0:
        div3 = div3 + 1
    if n % 7 == 0:
        div7 = div7 + 1

print("numeri maggiori di zero: {}\nnumeri divisibili per 3: {}\nnumeri divisibili per 7: {}".format(not0, div3, div7))