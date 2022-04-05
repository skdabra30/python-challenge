# PyPoll Challenge

# Import Modules
import os
import csv

# Create variables
candidates = []
numberof_votes = 0
vote_count = []

# Set path for csv file
csvpath = os.path.join("PyPoll/Resources","election_data.csv")

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip headers
    line = next(csvreader,None)

    # Process the votes
    for line in csvreader:

        # Increase count for total votes
        numberof_votes = numberof_votes + 1

        # Identify candidate receiving votes
        candidate = line[2]

        # Add to the candidate votes
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        
        # Else create new entry for new candidate receiving votes
        else:
            candidates.append(candidate)
            vote_count.append(1)

 # Variables for calculations
percentages = []
max_votes = vote_count[0]
max_index = 0

# Calculate percentage of votes for each candidate
for count in range(len(candidates)):
    vote_percentage = vote_count[count]/numberof_votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > max_votes:
        max_votes = vote_count[count]
        print(max_votes)
        max_index = count

# Determine winner
winner = candidates[max_index]

# Format numbers
percentages = [round(i,3) for i in percentages]

# Print analysis
print("Election Results")
print("--------------------------")
print(f"Total Votes: {numberof_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


# Open file
filewriter = open("electionanalysis.txt", mode = 'w')

# Print to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {numberof_votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

# Close file
filewriter.close()