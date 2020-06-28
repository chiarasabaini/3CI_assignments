__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020/02/22"

import random
from math import sin, cos, pi

def svg_random_polygons(n, width, height):
    """Restituisce un parte di documento SVG con n poligoni (meglio se regolari) casuali.
     In particolare, sono casuali: il colore di riempimento, il numero di lati,
     la lunghezza del lato (entro opportuni intervalli)."""
    
    svg = ""
    for i in range(n):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        size = random.randint(1, 20)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        wh = random.randint(0, 200)
        ht = random.randint(0, 200)
        
        svg += f"""
        <rect x="{x}" y="{y}"  width="{wh}" height="{ht}" strokewidth="1" stroke="#333" fill="rgb({r}, {g}, {b})"/>"""
        
    return svg

def write_svg_document(body, filename, width=800, height=600):
    """Scrive in un file un documento SVG"""
    
    svg_start = f"""<?xml version="1.0"?>
    <svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">"""

    svg_end = """
    </svg>
        """
    with open(filename, "w") as file:
         file.write(svg_start)
         file.write(body)
         file.write(svg_end)
     
if __name__ == "__main__":
 width, height = 800, 600
 body = svg_random_polygons(100, width, height)
 write_svg_document(body, "random_polygons.svg", width, height)