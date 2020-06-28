'''
program that makes conversion between temperature scales
@author Sabaini Chiara 3CI
@version 0.1 2019/11/24
'''

t = eval(input("insert temperature value (if it's a float value, please use the dot): "))

print("C = Celsius; F = Fahrenheit; K = Kelvin")

sc = input("insert scale: ")
conv = input("insert convertion's scale: ")

while sc != "C" and sc != "F" and sc != "K":
    print("ERROR: INVALID SCALE!")
    sc = input("please insert a valid scale: ")

while conv != "C" and conv != "F" and conv != "K":
    print("ERROR: INVALID SCALE!")
    conv = input("please insert a valid scale: ")

if sc == "C":
    if conv == "F":
        t = (t * (9 / 5)) + 32
    if conv == "K":
        t = t + 273.15
        
elif sc == "F":
    if conv == "C":
        t = (t - 32) * (5 / 9)
    if conv == "K":
        t = (t - 32) * (5 / 9) + 273.15
        
else:
    if conv == "C":
        t = t - 273.15
    if conv == "F":
        t = (t - 273.15) * (9 / 5) + 32

if conv == "C" or conv == "F":
    print(t, "°", conv)
else:
    print(t, conv)
