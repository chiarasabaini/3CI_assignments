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

def count_words(file):
    """Counts the words in a file
    """
    words = 0
    for line in open(file):
        linea = line.strip().split(" ")
        words += len(linea)
    return words

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
    print("Lines: ", count_lines(file))
    print("Words: ", count_words(file))
    print("Characters: ", count_chars(file))
    print("Times ", char," is shown: ", count_char(file, char)) 