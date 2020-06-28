__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2019/12/10"

def factorial(n):
    '''Returns the factorial of a number

    >>> factorial(5)
    120
    >>> factorial(11)
    39916800‬
    '''
    if n == 1:
        f = 1
    else:
        f = n  * factorial(n-1)
    
    return f

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)