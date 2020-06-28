__author__ = "Sabaini Chiara 3CI"
_version__ = "1.0 2020-03-22"

from random import randint, seed


def random_pairs1(start, end, blacklist):
    """Returns a list of couples of numbers in [start, end]
    without considering the elements in the blacklist.
    
    >>> seed(0)
    >>> random_pairs1(1, 25, [23, 25])
    [(13, 15), (2, 10), (21, 20), (17, 12), (9, 7), (18, 5), (19, 4), (11, 6), (24, 1), (22, 14), (16, 3)]
    """
    n = []
    couples = []
    
    for _ in range (start, end + 1):
        if start in blacklist :
            start += 1
        else :
            n.append(start)
            start += 1
    n.reverse()
    
    while n != [] :
        couple = []
        
        n1 = randint(0, n[0])
        if n1 not in n :
            while n1 not in n :
                n1 = randint(0, n[0])
        couples.append(n1)
        n.remove(n1)
        
        n2 = randint(0, n[0])
        if n2 not in n :
            while n2 not in n :
                n2 = randint(0, n[0])
        couples.append(n2)
        n.remove(n2)
        
        couples.append(couple)
        
        if len(n) == 1 :
            print("Couples: ", couples)
            print("C'è un numero che è rimasto solo, che è", n, ":(")
            exit()
            
    print("Couples =", couples)

if __name__ == "__main__":
    random_pairs1(1, 25, [23, 25])
    