from graphviz import Source

YELLOW ='\u001b[33m'
WHITE = '\u001b[37m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'

def print_argv():
    "Program files"
    from sys import arg

    for i in range(len(argv)):
        print(f"{YELLOW}{1:02d} {RED}{argv[i]}")
        print(F"{WHITE}\tDOT file viewer\n")
        print(f"{RED}SYNOPSIS")
        print(f"{RED}\tpython {WHITE}{__file__} {RED}{FILE}\n")

if __name__ == "__main__":
    print_argv()