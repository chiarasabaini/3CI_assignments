__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-05-07"

import time

def digital_clock():
    """Shows the current time on the terminal (without going on a new line).
    Uses the ANSI escape encoding to show in the terminal the data in different colors.
    Reference: https://en.wikipedia.org/wiki/ANSI_escape_code"""
    
    first, second = '\x1b[33m', '\x1b[31m'
    while True:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(first + result, end="", flush=True)
        print("\r", end="", flush=True)
        first, second = second, first
        time.sleep(1)

if __name__ == "__main__":
    digital_clock()