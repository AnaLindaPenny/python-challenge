import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print(csvpath)

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    print(csv_reader)

    





