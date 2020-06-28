'''
program that calculates the requested root of a number given by the user
@author Sabaini Chiara 3CI
@version 1.0 2019/11/23
'''

i = 1
j = 0
rad = 1

n = int(input("number: "))

while n <= 0:
    print("ERROR: INVALID NUMBER!")
    n = int(input("insert a valid number: "))
    
r = int(input("root: "))
while n <= 0:
    print("ERROR: INVALID ROOT!")
    r = int(input("insert a valid root: "))

while rad <= n:
    for j in range(r, 0 - 1, -1):
        rad = rad * i
    i = i + 1
        
print(i - 1)
