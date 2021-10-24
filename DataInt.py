import csv

rows = []

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

with open('Data_1.csv', r) as FileToCheck:
    csvreader = csv.reader(FileToCheck, delimiter = ',', lineterminator = '\r\n')

    headings = csvreader.next()

    for row in csvreader:
        rows.append(row)
        for i in range(len(row)):
            if (!isinstance(rows[i],float)):
                print("Invalid entry")
                quit()
            else if (row[i] == ' '):
                print("Invalid entry")
                quit()
            else 
                print("Valid file")
                
