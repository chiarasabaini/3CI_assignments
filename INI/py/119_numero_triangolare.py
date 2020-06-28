'''Programma che dice se un numero è triangolare oppure no, se è triangolare stampa il triangolo corrispondente
in ASCII art
@author Sabaini Chiara 3CI
@version 0.1 2019/12/02
'''

n = int(input("Inserisci numero: "))
i = 1
m = n
count = 0

while m > 0:
    m -= i
    i += 1
    
if m == 0:
    print("{} è un numero triangolare".format(n))
    for j in  range(i):
        tab_ = int(((i - j) / 2))
        print("\t" * tab_,"*\t" * j)
        
else:
    print("{} non è un numero triangolare".format(n))