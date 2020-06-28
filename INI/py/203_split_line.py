__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-24"

def split_line(line, sep=" "):
    """GIven a line (str that ends with \n)
    returns a list of its parts, using the given sep
    """
    d = 0
    c = ""
    res = []
    
    a = len(line)
    c += "'"

    for i in range(a - 1):
        if line[d] != sep :
            c += line[d]
            d += 1
        else :
            c += "'"
            c += ","
            c += sep
            c += "'"
            d += 1
    c += "'"
    res.append(c)
    print(res)

if __name__ == "__main__":
    split_line("34 7 19\n")