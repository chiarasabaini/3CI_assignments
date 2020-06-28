'''
program that prints the Pitagora's Table from 1 to n
(n is a number inserted by the user)
@author Sabaini Chiara 3CI
@version 0.1 2019/11/24
'''

n = int(input("number: "))

for i in range(1, n+1, 1):
    for j in range(1, 11, 1):
        print(i * j, end='\t')
    print("")
