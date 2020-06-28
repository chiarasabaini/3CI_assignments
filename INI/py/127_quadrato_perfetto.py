'''Realizza il programma quadrato_perfetto.py (senza funzioni) che, dato un numero intero n inserito
dall’utente, fornisce un output che indica se si tratta di un quadrato perfetto oppure no.
@author Sabaini Chiara 3CI
@version 0.1 2019/12/09
'''

n = int(input("Inserisci numero: "))
char = " # "
i = 0

while i < n:
    if i * i == n:
        print(n, " è un quadrato perfetto")
        
        for j in range(0, n):
            print(char  *  n)
        i =  n
    i += 1
    
if i == n:
    print(n, " non è un quadrato perfetto")