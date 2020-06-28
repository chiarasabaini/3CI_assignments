__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-05-11"

def fsa_even_parity(s, symbol='1', alphabet='01', check_input=False):
    """Returns True if s has an even number of occurrency of a simbol.
    Otherwise False.
    If it founds that doesn't belog to the specified alphabeth,
    raises an exception with the message 'Input simbol not valid'
    
    >>> fsa_even_parity("011101010", '0')
    True
    >>> fsa_even_parity("011101011", '1')
    True
    >>> fsa_even_parity("011101X010", '1')
    True
    >>> fsa_even_parity("011101X010", '1', check_input=False)
    False
    >>> from string import digits
    >>> fsa_even_parity("Python 4 all", "a", alphabet=digits)
    True
    """

    status = "S1"

    for char in s:
        if char in alphabet:
            pass
            if char == symbol:
                if status == "S1":
                    status = "S2"
                else:
                    status = "S1"
        elif check_input:
            alphabet_desc = str(tuple(alphabet)).replace("(", "{").replace(")", "}").replace("'", "")
            raise Exception(f"Input simbol not valid (alphabet = {tuple(alphabet_desc)})") # Runtime Error

    return status == "S1"

def input_string():
    """Executes parity controls on a string given in input.
    If the string is made of symbols that don't belong to the alphabet
    asks to the user to insert it again."""

    done = False

    while not done:
        try:
            s = input("String? ")

            if fsa_even_parity(s, check_input=True):
                print(f"The string {s} is valid")
            else:
                print(f"The string {s} is unvalid")
                
            done = True
        except:
            print("Chars unvalid. Reinsert the string.")

if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)
    input_string()