__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2020/01/11"

def is_palindrome(s):
    """Declares if a string is palindrome or not

    >>> is_palindrome("anna")
    True
    >>> is_palindrome("ann a")
    False
    """

    _s = s[::-1]

    return _s == s

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
