__author__ == "Sabaini CHiara 3CI"
__version__ == "1.0 2020-03-22"

def is_digit(a):
    """Returns True if a it's a number, False if it's not
    is_digit(20)
    True
    >>> is_digit("ciao")
    False
    """
    if type(a) == int :
        return True
    else :
        return False

if name == "main":
    import doctest
    doctest.testmod(verbose=True)