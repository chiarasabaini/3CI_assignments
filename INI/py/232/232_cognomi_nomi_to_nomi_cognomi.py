__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-30"

def reverse(file_in):
    """
    """
    output = ""
    for line in open(file_in):
        if len(line.split()) > 2:
            surname, name, _name = line.strip().split(" ")
            if len(surname) < 4:
                _surname = f"{surname} {name}"
                output += f"{_name} {_surname}"
        else:
            output += f"{name} {surname}"
if __name__ == "__main__":
    file_in = "data\\cognominomi.txt"