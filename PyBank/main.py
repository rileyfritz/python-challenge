# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to write to
output_path = os.path.join("Analysis", "new.txt")

# Define variables
csvpath = os.path.join('Resources', 'budget_data.csv')
month_count = 0
pl_total = 0
first_month_PL = 0
last_month_PL = 0
current_month_PL = 0
next_month_PL = 0
maxProfit = 0
maxProfitMonth = ""
maxLoss = 0
maxLossMonth = ""


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # go to first row after header
    csv_header = next(csvreader)
    
    # loop through csv file
    for row in csvreader:

        # get first month
        if month_count == 0:
            first_month_PL = float(row[1])

        # get month total, sum
        month_count += 1
        pl_total += float(row[1])

        #get max Profit, max Loss
        next_month_PL = float(row[1])        
        change = next_month_PL - current_month_PL
        current_month_PL = float(row[1])
        
        if change > maxProfit:
            maxProfit = change
            maxProfitMonth = row[0]
        if change < maxLoss:
            maxLoss = change
            maxLossMonth = row[0]

# get total change
last_month_PL = float(row[1])  
total_change = last_month_PL - first_month_PL

# get average change
average_change = (total_change) / (month_count - 1)

# Print Results
print('Financial Analysis')
print('-------------------')
print('\n')
print(f'Total Months: {month_count}')
print(f'Total: ${round(pl_total,0)}')
print(f'Average Change: ${round(average_change,0)}')
print(f'Greatest Profit Increase: {maxProfitMonth}: ${maxProfit}')
print(f'Greatest Profit Decrease: {maxLossMonth}: ${maxLoss}')

with open(output_path, 'w') as writer:
    writer.write('Financial Analysis')
    writer.write('\n')
    writer.write('-------------------')
    writer.write('\n')
    writer.write(f'Total Months: {month_count}')
    writer.write('\n')
    writer.write(f'Total: ${round(pl_total,0)}')
    writer.write('\n')
    writer.write(f'Average Change: ${round(average_change,0)}')
    writer.write('\n')
    writer.write(f'Greatest Profit Increase: {maxProfitMonth}: ${maxProfit}')
    writer.write('\n')
    writer.write(f'Greatest Profit Decrease: {maxLossMonth}: ${maxLoss}')