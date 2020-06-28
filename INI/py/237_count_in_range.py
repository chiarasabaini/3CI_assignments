__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-04-06"

def count_in_range(filename, a, b):
    """Conta i comuni con numero abitanti contenuto in [a, b]
    >>> count_in_range("data\\listacomuni.csv", 500000, 1000000)
    4
    """
    n_municipality = 0
    count = 0
    lines = open(filename, "r").readlines()
    
    for line in lines:
        words = line.strip().split(";")
        
        if count >= 1:
            if int(words[7]) >= a and int(words[7]) <= b:
                n_municipality += 1
        count += 1
    
    return n_municipality


if __name__ == "__main__":
    """
    import doctest
    doctest.testmod(verbose=True)
    """
    filename = "data\\listacomuni.csv"
    a = 500000
    b = 1000000
    print(count_in_range(filename, a, b))