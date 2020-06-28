'''Programma che restituisce il MCD di due numeri interi utilizzando l'algoritmo di Euclide,
testato usando il TDD
@author Sabaini Chiara 3CI
@version 0.1 2019/12/09
'''

def mcd(a, b):
    '''
    Restituisce il Massimo Comun Divisore di due numeri interi, utilizzando l'algoritmo di Euclide.

    >>> mcd(6, 12)
    6
    >>> mcd(30, 250)
    10
    '''
    while b != 0:
        res = a % b
        a = b
        b = res

    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)