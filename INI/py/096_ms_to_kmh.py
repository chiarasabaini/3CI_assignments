'''
programma che converte una velocità da m/s in km/h
@author Sabaini Chiara 3CI
@version 1.0 2019/11/18
'''

d = eval(input("inserisci la distanza in metri: "))
t = eval(input("inserisci il tempo in secondi: "))

v = round((d/t)*3.6, 2)

print("la velocità in è di", v, "km/h")

