def html_unordered_list(_list):
    """Restituisce una lista HTML"""

def write_html_document(body, filename, title):
    """Scrive in un file un documento HTML"""
    with open("list.txt") as file:
        file.write("<html>")

if __name__ == "__main__":
    _list = [
            ["Prehistory", "Pascal", "Leibniz"],
            ["Modern times", "Zuse", "von Neumann", "Turing"],
            ["Contemporary times", "Ritchie", "Wirth", "van Rossum"]
        ]
    body = html_unordered_list(_list)
    write_html_document(body, "html_list_cs_legends.html", "(uncomplete) Computer Science Legends of all times")