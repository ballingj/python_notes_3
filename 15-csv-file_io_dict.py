import csv

desired_wage = 40000
high_wages = []
with open('wages.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    for elem in reader:
        print(elem)  # <= Each of these elements are `dict`s, not `list`s!
        if int(elem['annual_wage']) >= desired_wage:
            high_wages.append(elem)
print(high_wages)
# high_wages is a list of dicts, which is helpful because each dict knows the meaning of each of its values!
# [{'id': '200', 'title': 'Salesperson', 'annual_wage': '40000'}, {'id': '500', 'title': 'Backend Engineer', 'annual_wage': '50000'}, 
# {'id': '512', 'title': 'Product Lead, Eng', 'annual_wage': '80000'}, {'id': '999', 'title': 'Accountant', 'annual_wage': '60000'}]

with open('high-wages-with-header.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=high_wages[0].keys())
    writer.writeheader()
    for elem in high_wages:
        writer.writerow(elem)  # Notice that we're passing a dict to writerow.

