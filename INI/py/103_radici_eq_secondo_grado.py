'''
programma che risolve equazioni di secondo grado
@author Sabaini Chiara 3CI
@version 0.1 2019/11/26
'''

a = eval(input("inserisci valore di a: "))
b = eval(input("inserisci valore di b: "))
c = eval(input("inserisci valore di c: "))

delta = (b ** 2) - (4 * a  * c)

if delta > 0:
    res = (- b + delta ** (1 / 2)) / (2 * a)
    res0 = (- b - delta ** (1 / 2)) / (2 * a)
    print(res, "; ", res0)
    
elif delta < 0:
    res = "Le soluzioni di questa equazione non sono comprese all'interno dell'insieme dei numeri reali"
    print(res)
else:
    res = - (b / (2 * a))
    print(res)
