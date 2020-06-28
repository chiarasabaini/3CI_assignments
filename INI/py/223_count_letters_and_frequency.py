__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-23"

import string

def count_chars(file):
    """Counts the characters in a file
    """
    with open(file, 'r') as file:
        data = file.read()
    return len(data)

def count_char(file, char):
    """Counts the time a character is shown in a file
    """
    count = 0
    
    for line in open(file):
        line = line.strip()
        
        for _char in line:
            if _char == char or char == None:
                count += 1
    return count

if __name__ == "__main__":
    file = "data\\divina_commedia.txt"
    char = "a"
    print("Characters: ", count_chars(file))
    print("Times ", char," is shown: ", count_char(file, char)) 