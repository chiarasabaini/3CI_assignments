'''
programma che calcola la somma dei primi n numeri naturali con due metodologie differenti 
@author Sabaini Chiara 3CI
@version 0.1 2019/12/02
'''

n = int(input("inserisci un numero: "))
sum_ciclo = 0
sum_formula = (n * (n + 1)) // 2
  
for i in range(1, n + 1, 1):
    sum_ciclo = sum_ciclo + i

print("somma ciclo = somma formula")
print("{} = {}".format(sum_ciclo, sum_formula))