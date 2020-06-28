'''Program that calculates the sum of the figures' values of a number, using TDD.
@author Sabaini Chiara 3CI
@version 0.1 2019/12/07
'''

def sum_figures(n):
    '''
    Returns the sum of the figures' values of a number
    >>> sum_figures(123)
    6
    >>> sum_figures(75)
    12
    '''
    _sum = 0
    while n > 0:
        _sum += n % 10
        n = n // 10
    return _sum

if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)
