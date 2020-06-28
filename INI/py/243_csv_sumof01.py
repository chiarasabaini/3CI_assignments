def csv_sumof(filename, field, sep=","):
    """Returns the sum of the values of the field's column
    for all the records in the CSV file specified.
    """
    file = open(filename, "r")
    
    
if __name__ == "__main__":
    filename = "data/istat_Institutions_with_volunteers.csv"
    value = csv_sumof(filename, ["Verona", "Mantova"], 5)
    print("Numero di istituzioni di volontariato: ", value)