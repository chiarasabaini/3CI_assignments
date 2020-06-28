__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-23"

def count_diphthongs(file):
    vowels = ["a", "e", "i", "o", "u", "à", "è", "é", "ì", "ò", "ù"]
    with open(file, 'r', encoding='utf-8' ) as file:
        diphthongs = 0
        tmp = 0
        letters = file.read().lower()
        for i in letters:
            if i in vowels and tmp == 1:
                diphthongs += 1
                tmp = 0
            if i in vowels:
                tmp = 1
            else:
                tmp = 0
    return diphthongs

if __name__ == "__main__":
    file = "data\\divina_commedia.txt"
    print("Diphthongs: ", count_diphthongs(file))