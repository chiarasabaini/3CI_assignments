__author__ = "Sabaini Chiara 3CI"
__version__ = "0.1 2019/12/09"

def triangolo_numerico(n):
     """Scrive per righe con colonne crescenti i numeri naturali da 1 a n.

     >>> triangolo_numerico(15)
      1
      2  3
      4  5  6
      7  8  9 10
     11 12 13 14 15
     """

     count = 1
     i = 1

     while i <= n:
          for j in range(count):
               print("{:>2}".format(i), end=" ")
               i += 1
          count += 1
          print()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)