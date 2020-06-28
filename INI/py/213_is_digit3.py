__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-22"

import string

def is_digit(a):
    """Returns True if a is a number, False if it's not
    
    >>> is_digit("3")
    True
    >>> is_digit("A")
    False
    >>> is_digit("4") == "4".isdigit()
    True
    >>> is_digit(4)
    True
    """
    
    try :
        res = a in string.digits and len(a) == 1
    except :
        res = type(a) == int and 0 <= a <= 9
    
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)