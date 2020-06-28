__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-05-11"

def fsa_even_parity(s, check_input=False):
    """Returns True if s has an even number of occurrency of a simbol.
    Otherwise False.
    If it finds a char that doesn't belogs to the alphabet {'0', '1'}
    raises an exception with the message 'Input simbol invalid'.
    
    >>> fsa_even_parity("011101010")
    True
    >>> fsa_even_parity("011101011")
    True
    >>> fsa_even_parity("011101X010")
    True
    >>> fsa_even_parity("011101X010", check_input=True)
    False
    """

    status = "S1"

    for char in s:
        if char == "1":
            pass
        elif char == "0":
            if status == "S1":
                status = "S2"
            else:
                status = "S1"
        elif check_input:
            raise Exception(f"Input simbol invalid (alphabet = {0, 1})") # Runtime Error

    return status == "S1"

def input_string():
    """Executes parity controls on a string given in input"""

    done = False

    while not done:
        try:
            s = input("String? ")

            if fsa_even_parity(s, check_input=True):
                print(f"The string {s} is valid")
            else:
                print(f"The string {s} is unvalid")
                
            done = True
        except Exception as e:
            print(e.args[0])

if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)
    input_string()