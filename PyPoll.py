# What we need...
#   1. Total number of votes cast
#   2. Complete list of candidates that got votes
#   3. Total and Percentage of votes per candidate
#   4. The winner based on popular vote

# Add dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("G:\Modules\Module_3\Election-Analysis\Resources\election_results.csv")

 # Assign a variable to save the file to a path.
file_to_save = os.path.join("G:\Modules\Module_3\Election-Analysis\Analysis\election_analysis.txt")

#1. Create vote counter that starts at zero
total_votes = 0

# Candidate options (list)
candidate_options = []

# Candidate votes (dict)
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the .csv file.
    for row in file_reader:
        # Add to the vote count
        total_votes += 1

        # Print candidate's name from each row
        candidate_name = row[2]

        # If name does not match any others, add it to options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

        # Begin tracking candidate's vote count, with each starting at zero
            candidate_votes[candidate_name] = 0
        # and add them as they are counted
        candidate_votes[candidate_name] += 1

# Print the total votes
print(candidate_votes)

# Close the file.
election_data.close()

# Calcualte vote percentages for each candidate
# Loop through the counts
for candidate_name in candidate_votes:

    # Define votes and retrive counts
    votes = candidate_votes[candidate_name]

    # Calculate percentage
    vote_percentage = (votes / total_votes) * 100

    # Print each candidate's vote percentages
    print(f"{candidate_name} recieved {vote_percentage:.2f}% of the vote!")

# start at 3.5.5