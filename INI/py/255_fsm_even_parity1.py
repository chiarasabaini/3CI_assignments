__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-05-11"

def fsa_even_parity0(s, check_input=False):
    """Returns True if s has an even number of occurrency of a simbol.
    Otherwise False.
    
    >>> fsa_even_parity0("011101010")
    True
    >>> fsa_even_parity0("011101011")
    True
    >>> fsa_even_parity0("011101X010")
    True
    >>> fsa_even_parity0("011101X010", check_input=True)
    False
    """

    status = "S1"

    for char in s:
        if char == 0:
            if status == "S1":
                status = "S2"
            else:
                status = "S1"
        elif check_input:
            status = False

    return status == "S1"

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)