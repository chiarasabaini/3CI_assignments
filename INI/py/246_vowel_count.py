__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-05-06"

vowels = "aeiou"

def text_vowel_count(text):
    """Counts the vowels in a text"""
    count = 0
    text.lower()
    for char in text:
        if char in vowels:
            count += 1 

    return count

def vowel_count(file):
    """Counts the vowels in a file"""
    lines = 0
    consonants = 0
    
    for line in open(file):
        lines += len(line)
        line = line.strip(vowels)
        consonants += len(line)

    return lines - consonants

if __name__ == "__main__":
    text = "Hello, world!"
    file = "data\\divina_commedia.txt"
    print("Vowels in text: ", text_vowel_count(text))
    print("Vowels in file: ", vowel_count(file))