import csv
import os

csvpath = os.path.join('Resources', "election_data.csv")


total_votes = 0
winner = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_list = []
candidate_votes = {}



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

    for row in csvreader:
        total_candidates = row[2]        
        total_votes = total_votes + 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_votes[row[2]] = 1

        if (total_votes > winner):
            greatest_votes[1] = candidate_votes
            greatest_votes[0] = row[2]
    
    
    for candidate in candidate_votes:
        print(candidate + " " + str(round((candidate_votes[candidate]/len(total_votes),2)" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round((candidate_votes[candidate]/len(total_votes),2)" + " (" + str(candidate_votes[candidate]) + ")") 
    
winner = sorted(candidate_votes.items(),)

print("Election Results")
print("")
print("Total Votes " + str(total_votes))
print("")
print("")
print("Winner: " + str(winner[1]))
print("")

