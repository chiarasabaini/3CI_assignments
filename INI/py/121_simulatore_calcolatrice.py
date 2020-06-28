__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2019/12/23"

def mycalc(exp):
    '''Simula una calcolatrice, restituendo il risultato,
    calcolato con eval(), dell'espressione fornita.
    Prevede un Easter Egg per un dato input.

    >>> mycalc(2 + 2)
    4

    >>> mycalc(3 ** 2 + 5)
    14

    >>> mycalc(4 * 7 + (2 ** 8))
    284
    '''
    exp = str(exp)
    if exp == "egg":
        exp =   "  .'''.\n /     \ \n:       :\n:       :\n `.___,' "

    else:
        exp = eval(exp)

    return exp

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) 