__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020/04/20"

with open("country_data_reduced.md", "w") as file_out:
    md = ""
    
    file_out.write(md)
    
if __name__ == "__main__":
    md = csv_to_markdown_table("country_data_reduced.csv")