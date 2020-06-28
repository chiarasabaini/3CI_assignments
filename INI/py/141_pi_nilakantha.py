__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2019/12/23"

def pi_nilakantha(n):
    """Ritorna il valore approssimato di pi greco utilizzando 
     la formula di Nilakantha fino all'n-simo termine della serie.

    >>> pi_nilakantha(3)
    3.141
    
    >>> pi_nilakantha(5)
    3.14159
    """
    i = 2
    j = 3
    k = 4
    pi = 3
    for _ in range(n + 1):
        pi = pi + ((-1) ** (-_)) * (4 / (i * j * k))
        i += 1
        j += 1
        k += 1

    return round(pi, n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
