'''
program that prints all the odd numbers from 1 to n
(n is a number inserted by the user)

@author Sabaini Chiara 3CI
@version 0.1 2019/11/24
'''

n = int(input("number: "))

#this loop prints all the odd numbers from 1 to n
for i in range(1, n+1, 2):
    print(i)
