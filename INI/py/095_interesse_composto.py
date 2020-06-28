'''
programma che dati in input i valori del capitale iniziale, il tasso di interesse e
gli anni, fornisce in output il capitale finale, utilizzando la formula per
l'interesse composto
@author Sabaini Chiara 3CI
@version 1.0 2019/11/18
'''

ci = eval(input("capitale iniziale: "))
ti = eval(input("tasso d'interesse (%): "))/100
time = eval(input("anni: "))

cf = round(ci*(1+ti)**time, 2)
print("capitale finale: ", cf, " euro")
