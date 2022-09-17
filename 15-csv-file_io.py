import csv

high_wages = []
desired_wage = 40000

with open('wages.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header line.
    for row in reader:
        annual_wage = int(row[2])  # (A)
        if annual_wage >= desired_wage:
            high_wages.append(row)

with open('high-wages.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    for row in high_wages:
        writer.writerow(row)
