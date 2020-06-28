__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-05-07"

def bubble_sort1(values):
    """Orders "in place" the list given in input, using bubble sort.
    >>> values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> bubble_sort1(values)
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
    values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubble_sort1(values))