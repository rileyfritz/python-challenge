# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
month_count = 0
pl_total = 0
first_month_PL = 0
last_month_PL = 0
current_month_PL = 0
next_month_PL = 0
maxProfit = 0
maxLoss = 0

# profits_losses = {}



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
        current_month_PL = float(row[1])
        next_month_PL = float(csvreader)
        
        


        # # Create P&L dictionary to find max and min

        # profits_losses.update({row[0]:float(row[1])})

# get total change
last_month_PL = float(row[1])  
total_change = last_month_PL - first_month_PL

# get average change
average_change = (total_change) / (month_count - 1)

# # get max and min
# def getmaxandmin(dictionary):
#     profitsAndLossesList = list(dictionary.values())
#     monthsList = list(dictionary.keys())
#     getmaxandmin.monthMaxProfit = monthsList[profitsAndLossesList.index(max(profitsAndLossesList))]
#     getmaxandmin.maxProfit = max(profitsAndLossesList)
#     getmaxandmin.monthMaxLoss = monthsList[profitsAndLossesList.index(min(profitsAndLossesList))]
#     getmaxandmin.maxLoss = min(profitsAndLossesList)

# # run max and min funciton with P&L dictionary
# getmaxandmin(profits_losses)

# Print Results
print('Financial Analysis')
print('-------------------')
print('\n')
print(f'Total Months: {month_count}')
print(f'Total: ${pl_total}')
print(f'Average Change: ${round(average_change,2)}')
# print(f'Largest Profit Increase: {getmaxandmin.monthMaxProfit} - {getmaxandmin.maxProfit}')
# print(f'Largest Profit Decrease: {getmaxandmin.monthMaxLoss} - {getmaxandmin.maxLoss}')