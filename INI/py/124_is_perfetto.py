'''Programma che dice se un numero è perfetto o no, testato usando il TDD
@author Sabaini Chiara 3CI
@version 0.1 2019/12/09
'''

def is_perfetto(n):
    '''Ritorna True se n è perfetto, False in caso contrario
    >>> is_perfetto(6)
    True
    >>> is_perfetto(10)
    False
    '''

    div = 2
    sum_ = 1

    while div <= n / 2:
        if n % 2 == 0:
            sum_ = sum_ + div
        div += 1

    return sum_ == n

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)