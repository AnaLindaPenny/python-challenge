import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print(csvpath)

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    headers = next(csvreader)

    print(headers)

total_months = 0
total_profit_losses = 0
previous_profit_losses = 0
average_change = 0
profit_losses_change = 0
profit_losses_changes = []

greatest_inc = ['', 0]
greatest_dec = ['', 9999999999]
profit_losses_changes = []

inputFile = os.path.join('..', 'Resources', 'budget_data.csv')

with open(inputFile) as FinancialAnalysisData:
    reader = csv.DictReader(FinancialAnalysisData)

    for row in csvreader:
        total_months = total_months + 1
        total_profit_losses = total_profit_losses + int(row['Profit/Losses'])

        if (previous_profit_losses != 0):
            profit_losses_losses_change = int(row['Profit/Losses']) - previous_profit_losses

        previous_profit_losses = int(row['Profit/Losses'])
    print(row)

output_path = os.path.join('..', 'PyBank', 'Analysis', 'financial_analysis_data.txt')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Date', 'Profit/Losses'])







