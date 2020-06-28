'''
stampa il risultato di 2**n, n è inserito dall'utente
@author Sabaini Chiara 3CI
@version 0.1 2019/12/02
'''
n = int(input("inserisci un numero: "))
res = 2

while n <= 0:
    print("ERRORE: INPUT NON VALIDO!")
    n = int(input("perfavore inserisci un numero intero maggiore di 0: "))

for i in range(1, n + 1, 1):
    res = res * 2

print("2 ** {} = {}".format(n, res))