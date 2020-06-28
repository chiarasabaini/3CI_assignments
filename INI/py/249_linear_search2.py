__author__ = "chiara@sabaini.com"
__version__ = "1.0 2020/05/06"

def linear_search2(values, value):
    """Searchs for a value in a given list, using the linear search.
    If the value exist, returns the index of the first position in the list,
    otherwise returns -1.
    
    >>> values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> linear_search2(values, 44)
    6
    >>> linear_search2(values, 52)
    -1
    >>> values = [54, 26, 93, 17, 77, 31, 44, 55]
    >>> linear_search2(values, 17)
    3
    """
    for i, _value in enumerate(values):
        if _value == value:
            return i

    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)