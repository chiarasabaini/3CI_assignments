'''
program that prints the Pitagora's Table from 1 to n
(n is a number inserted by the user)
@author Sabaini Chiara 3CI
@version 0.1 2019/11/30
'''

n = int(input("number: "))
i = 1

while i <= n:
    j = 1
    while j <= 10:
        print(i * j, end='\t')
        j = j + 1
    i = i + 1
    print("")
