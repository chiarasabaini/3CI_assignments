__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0"
__date__ = "2020-03-30"

def txt_to_csv(file_in, file_in1, file_out):
    """
    """
    file = open(file_in, "r").readlines()
    file1 = open(file_in1, "r").readlines()
    out = open(file_out, "w")
    output = "Name,Surname,E-mail\n"
    names = []
    emails = []
    for line in file:
        names += line
    for line in file1:
        emails += line
    
    for i in range(len(names)):
        output += f"{names[i]},{emails[i]}\n"

    out.write(output)

if __name__ == "__main__":
    file_in = "data\\cognominomi.txt"
    file_in1 = "data\\emails.txt"
    file_out = "data\\names_emails.csv"
    txt_to_csv(file_in, file_in1, file_out)