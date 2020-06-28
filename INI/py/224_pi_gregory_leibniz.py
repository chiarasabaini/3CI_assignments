'''Restituisce il valore di pi greco
utilizzando la serie di Gregory-Leibniz fino all'n-simo valore
@author Sabaini Chiara 3CI
@version 0.1 2019/12/09
'''

def pi_gregory_leibniz(n):
    """Restituisce il valore di pi greco
     utilizzando la serie di Gregory-Leibniz fino all'n-simo valore
     
     >>> pi_gregory_leibniz(10)
     3.232315809405594
     """
     
    pi = 1
     
    pi = pi +(((-1) ** i) / (2 * i + 1))
    
    return pi * 4

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
