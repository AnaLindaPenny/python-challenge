import os
import csv

inputFile = os.path.join('..', 'Resources', 'election_data.csv')
csvpath = os.path.join('election_data.csv')

# Need to define the variables
total_votes = 0 
candidate_list = []
candidate_dict = {}

winning_vote = 0 
winner = ''

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    reader = csv.reader(csvfile)
    next(reader, None)

    for row in reader:
        # Need to count the total votes    
        total_votes += 1 
        
        # Need to reference candidate name from the row 
        candidate = row[2]

        if candidate not in candidate_list:
        # Need to add the candidate to the candidate list 
            candidate_list.append(candidate)
            candidate_dict[candidate] = 0

            
            candidate_dict[candidate] +=1 

output_file = 'Analysis/election_results_data.txt'
with open(output_file, 'w', newline='') as datafile:
    
    print(f'Election Results')
    print(f'--------------------')
    print(f'Total Votes: {total_votes}')
    print(f'--------------------')

    datafile.write(f'Election Results\n')
    datafile.write(f'--------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write(f'--------------------\n')
    
    # Need to loop through the candidates and calculate their percentage of the votes 
    for candidate in candidate_dict: 
        percentage = round(float(candidate_dict[candidate])/float(total_votes),2)

    print(f'{candidate}: {percentage:.3%} ({candidate_dict[candidate]})\n')
    datafile.write(f'{candidate}: {percentage:.3%} ({candidate_dict[candidate]})\n')

    votes = candidate_dict[candidate]
    if votes > winning_vote:
            winning_vote = votes
            winner = candidate

    # Print the results to the terminal and the txt file       
    print(f'--------------------')
    print(f'Winner: {winner}')
    print(f'--------------------')
    datafile.write(f'--------------------\n')
    datafile.write(f'Winner: {winner}\n')
    datafile.write(f'--------------------')



