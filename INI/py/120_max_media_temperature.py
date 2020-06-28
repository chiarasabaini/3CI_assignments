'''Programma che stampa la media e il massimo valore di un elenco di temperature
@author Sabaini Chiara 3CI
@version 0.1 2019/12/02
'''

temp = [30.7, 32.2, 33, 33.2, 28.6, 27.5, 30.7, 32.4, 34.5, 32.8, 29.3]
max_ = 0
media = 0

for i in range(0, 11, 1):
    if max_ < temp[i]:
        max_ = temp[i]
        
    media = media + temp[i]

media = round(media/11, 2)

print("La media tra i valori {} è {}, il valore massimo è {}".format(temp, media, max_))