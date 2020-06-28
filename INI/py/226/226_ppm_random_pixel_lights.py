__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-24"

import string
import random

def create_ppm(file, w, h, n, bgcolor, fgcolor):
    """Creates a PPM P3 width x height image,
    with n casual pixels on
    """
    count = 0
    magic_word = "P3"
    body = ""
    header = f"{magic_word}\n{w} {h}\n255\n"
    pos = []
    
    for i in range(n):
        pos.append(random.randint(0, w * h - 1))
    
    for j in range(h):
        for _ in range(w):
            if count in pos :
                body += f"{fgcolor}\n"
            else :
                body += f"{bgcolor}\n"
            
            count += 1
    
    data = header + body
    with open (file, "w") as file:
        file.write(data)
        file.close()
    
if __name__ == "__main__":
    file = "random_pixel_lights.ppm"
    create_ppm(file, 400, 300, 2000, (0, 0, 0), (255, 255, 0))