__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-24"

import string
import random

def create_ppm(file, w, h):
    """Creates a PPM P3 width x height image,
    with random colored pixels
    """
    file = open(file, "w")
    
    magic_number = "P3"
    color = 255
    
    header = f"{magic_number}\n{w} {h}\n{color}\n"
    data = ""
    
    for i in range(h):        
        for j in range(w):
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            data+= f"{r} {g} {b}\n"
    
    file.write(header)
    file.write(data)
    file.close()
    
if __name__ == "__main__":
    file = "quads.ppm"
    create_ppm(file, 500, 400)