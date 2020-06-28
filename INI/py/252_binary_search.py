__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-05-07"

def binary_search(values, value):
    """Searches a value in a list given in input, using the binary (or dichotomy) search.
    If the value exist returns the index of the first position in the list,
    otherwise returns -1.

    >>> values = [54, 26, 93, 17, 77, 31, 44, 55, 20] # Numero di valori dispari
    >>> binary_search(values, 44)
    4
    >>> binary_search(values, 52)
    -1
    >>> values = [54, 26, 93, 17, 77, 31, 44, 55] # Numero di valori pari
    >>> binary_search(values, 44)
    3
    """
    values = bubble_sort(values)

    x = len(values) // 2

    if values[x] == value:
        return x
    elif values[x] > value:
        y = x
        x = 0
        for j in range(0, y):
            if values[x] == value:
                return x
            else:
                x += 1

    return -1

def bubble_sort(values):
    """Orders "in place" the list given in input, using bubble sort.
    >>> values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> bubble_sort(values)
    [17, 20, 26, 31, 44, 54, 55, 77, 93] 
    """

    for i in range(len(values)):
        for j in range(len(values) - 1):
            if values[j] > values[j + 1]:
                maj = values[j]
                values[j] = values[j + 1]
                values[j + 1] = maj

    return values

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)