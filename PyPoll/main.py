# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Specify the file to write to
output_path = os.path.join("Analysis", "Poll_Results.txt")

# Specify file to read from
csvpath = os.path.join('Resources', 'election_data.csv')


# Variables 
vote_count = 0
candidate_list = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # go to first row after header
    csv_header = next(csvreader)
    
    # loop through csv file
    for row in csvreader:
        
        # get total vote count
        vote_count += 1

        # get list of candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])



print(vote_count)

