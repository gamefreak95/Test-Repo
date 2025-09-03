import csv

with open('names.csv', 'r') as rf:
    csv_reader = csv.DictReader(rf)

    with open ('new_names.csv', 'w') as wf:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(wf, fieldnames=fieldnames, delimiter="|")

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)