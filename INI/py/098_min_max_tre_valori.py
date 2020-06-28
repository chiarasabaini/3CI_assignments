'''
programma che restituisce in output il numero più grande e quello più piccolo,
tra i 3 inseriti in input
@author Sabaini Chiara 3CI
@version 1.0 2019/11/18
'''

print("Inserisci primo numero:")
n0 = int(input())

print("Inserisci secondo numero:")
n1 = int(input())

print("Inserisci terzo numero:")
n2 = int(input())

if n0 > n1 and n0 > n2:
    print("max: ", n0)
    if n1 > n2:
        print("min: ", n2)
    else:
        print("min: ", n1)
            
elif n1 > n0 and n1 > n2:
    print("max: ", n1)
    if n0 > n2:
        print("min: ", n2)
    else:
        print("min: ", n0)
            
elif n2 > n1 and n2 > n0:
    print("max: ", n2)
    if n1 > n0:
        print("min: ", n0)
    else:
        print("min: ", n1)
