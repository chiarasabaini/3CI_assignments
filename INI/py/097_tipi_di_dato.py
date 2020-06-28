'''
programma che fornisce informazioni riguardo al datatype del dato inserito nella
variabile d
@author Sabaini Chiara 3CI
@version 1.0 2019/11/18
'''
import ast

d = type(ast.literal_eval(input("inserisci dato [se è una sequenza di caratteri, inserirla tra doppi apici(eccetto True, False)]: ")))

print(d)
