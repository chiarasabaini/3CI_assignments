__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-12"

def is_digit(a):
    """Returns True if a is a number, False if it's not
    >>> is_digit(20)
    True
    >>> is_digit("spam and eggs")
    False
    """
    if type(a) == int :
        return True
    else :
        return False
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)