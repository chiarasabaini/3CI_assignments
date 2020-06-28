__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-23"

import string

def count_lines(file):
    """Counts the lines in a file
    """
    lines = 0
    with open(file, 'r') as file:
        for line in file:
            lines += 1
    return lines

if __name__ == "__main__":
    file = "data\\divina_commedia.txt"
    print("Lines: ", count_lines(file))