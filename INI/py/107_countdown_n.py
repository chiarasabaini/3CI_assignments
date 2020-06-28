'''
program that prints a countdown from n to 1
(n is a number inserted by the user)

@author Sabaini Chiara 3CI
@version 0.1 yyyy/mm/dd
'''

n = int(input("number: "))

#this loop prints all the number from n to 1
for i in range(n, 0, -1):
    print(i)
