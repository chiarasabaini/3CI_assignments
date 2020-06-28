__author__ = "chiara@sabaini.com"
__version__ = "1.0 2020/05/06"

# Wikipedia Link: https://it.wikipedia.org/wiki/Selection_sort

def selection_sort(values):
    """Orders "in place" the list given in input, using the selection sort

    >>> values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> selection_sort(values)
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    
    for i in range(len(values)):
        min_pos = i
        min_value = values[i]

        for j in range(min_pos, len(values)):
            if values[j] < min_value:
                min_pos = j
                min_value = values[j]
               
        values[i], values[min_pos] = values[min_pos], values[i]

    return values

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)