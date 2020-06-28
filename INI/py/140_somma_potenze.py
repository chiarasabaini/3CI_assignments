__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2019/12/22"

def potenza(n, esp):
    '''Data una base e un esponente ritorna la relativa potenza,
    utilizzando un ciclo.
    
    >>> potenza(2, 5)
    32
    >>> potenza(6, 3)
    216
    '''
    p = 1
    for _ in range(1, esp + 1):
        p = p * n
    
    return p

def sum_potenze(base, n):
    '''Ricevuti due valori (base e n),
    utilizza la funzione potenza() per calcolare
    e ritornare la somma di tutte potenze di base da 0 a n.

    >>> sum_potenze(2, 3)
    15
    '''

    sum = 0

    for i in range(0, n + 1):
        sum += potenza(base, i)

    return sum

    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)