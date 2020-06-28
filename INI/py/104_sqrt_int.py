'''
program that calculates the square root of a number given by the user
@author Sabaini Chiara 3CI
@version 1.0 2019/11/23
'''
n = int(input("number: "))
i = 1

while n <= 0:
    print("ERROR: INVALID NUMBER!")
    n = int(input("insert a valid number: "))

while i*i <= n:
    i += 1
i -= 1
print("sqrt(", n, ")=", i)
