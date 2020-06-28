__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-03-24"

def unppmzip(file_in, ):
    """Unzipping a PPM file
    """
    lines = open(file_in, encoding="utf8").readlines()
    
    magic_number = lines[0]
    dimensions = lines[1]
    max_color = lines[2]
    
    header = f"{magic_number}{dimensions}{max_color}"
    data = ""

    for line in lines[3:]:
        r, g, b, n= line.split(sep)
        
        for _ in range(int(n)):
            data += f"{r}{g}{b}\n"

    file_out = open(file_out, "w")
    file_out.write(header)
    file_out.write(data)
    file_out.close()

if __name__ == "__main__":
    file_in = "simple2.ppm"
    file_out = "simple2.ppmzip"
    