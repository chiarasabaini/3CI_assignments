__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2020/01/11"

def str_inverse(s):
    """Gives as output the string reversed

    >>> str_inverse("ciao")
    'oaic'
    >>> str_inverse("yellow sunflower")
    'rewolfnus wolley'
    """
    
    _s = s[::-1]

    return _s

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
