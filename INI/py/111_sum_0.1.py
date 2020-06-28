'''
programma che somma 0.1 per n volte, stampa i risultati intermedi e il risultato finale
@author Sabaini Chiara 3CI
@version 0.1 2019/12/02
'''

n = int(input("inserisci numero: "))
sum = 0

for i in range(n):
    sum = round(sum + 0.1, 1)

print(sum)
