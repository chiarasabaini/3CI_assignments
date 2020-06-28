__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2019/12/22"

def sum_odd(n):
    '''calcola la somma dei primi n numeri naturali dispari
    con due metodologie differenti

    >>> sum_odd(3)
    (9, 9)
    >>> sum_odd(12)
    (144, 144)
    '''
    sum_ciclo = 0
    sum_formula = n ** 2
    i = 0
    j = 0
    while i < n:
        if j % 2 == 1:
            sum_ciclo = sum_ciclo + j
            i += 1
        j += 1

    return sum_ciclo, sum_formula

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)