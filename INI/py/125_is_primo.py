'''Program that says if a number is prime or not
@author Sabaini Chiara 3CI
@version 0.1 2019/12/10
'''

def is_primo(n):
    '''Restituisce True se n è primo, False in caso contrario

    >>> is_primo(2)
    True
    >>> is_primo(12)
    False
    '''
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)