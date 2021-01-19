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
most_votes = 0
candidate_list = []
candidate_votes_dict = {}
all_votes = []


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

        # Put all votes in a list
        all_votes.append(row[2])
    
    # Print vote count
    print(f'There were {vote_count} votes during this election!')

    # create dictionary with each candidate and vote count
    for candidate in candidate_list:
        votes_recieved = all_votes.count(candidate)
        candidate_votes_dict[candidate] = all_votes.count(candidate)
        # Looking for the winner
        if votes_recieved > most_votes:
            most_votes = votes_recieved
            winning_candidate = candidate
        # print out results to terminal
        print(f'{candidate} received {votes_recieved} votes ({round((votes_recieved / vote_count) * 100, 0)}%)')
        
    # Print winner
    print(f'{winning_candidate} is the winner!')
    
with open(output_path, 'w') as txtfile:
    for candidate, votes in candidate_votes_dict.items():
        txtfile.write(f'{candidate} recieved {votes} votes')
        writer.write('\n')


