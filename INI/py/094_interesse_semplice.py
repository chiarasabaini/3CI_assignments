'''
programma che , dati in input i valori del capitale iniziale, il tasso di interesse
e il tempo, fornisce in output il capitale finale
@author Sabaini Chiara 3CI
@version 1.0 2019/11/18
'''

ci = eval(input("inserisci il tuo capitale di partenza: "))
ti = eval(input("inserisci il tasso di interesse: "))
time = eval(input("inserisci il tempo in anni: "))

cf = round(ci+(ci*ti*time)/100, 2)
print("il capitale finale ammonta a ", cf, "euro")
