__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-23"

def crypt(str, key):
    '''Crypts the string given in input
    >>> crypt("ATTACCARE I GALLI PRIMA CHE BEVANO LA POZIONE MAGICA", 3)
    dwwdffduh l jdool sulpd fkh ehydqr od srclrqh pdjlfd
    '''
    w = ""
    cipherValue = []

    for ch in str.lower():

        n = 0
        ordValue = ord(ch)

        if ordValue <= 120:
            cipherValue.append(ordValue + key)
        else:
            cipherValue.append(ordValue - (26 - key))
        n = n + 1


    for n in cipherValue:
        crypto = chr(n)
        if crypto == "#":
            crypto = " "
        print(crypto, end='')

def decrypt(str, key):
    '''Crypts the string given in input
    >>> decrypt("dwwdffduh l jdool sulpd fkh ehydqr od srclrqh pdjlfd", 3)
    attaccare i galli prima che bevano la pozione magica
    '''
    w = ""
    cipherValue = []

    for ch in str.lower():

        n = 0
        ordValue = ord(ch)

        if ordValue <= 120:
            cipherValue.append(ordValue + key)
        else:
            cipherValue.append(ordValue - (26 - key))
        n = n + 1


    for n in cipherValue:
        crypto = chr(n)
        if crypto == "#":
            crypto = " "
        print(crypto, end='')

if __name__ == "__main__":
    crypt("ATTACCARE I GALLI PRIMA CHE BEVANO LA POZIONE MAGICA", 3)
    import doctest
    doctest.testmod(verbose=True)