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

# Winning candidate and winning count tracker
# Declare winning candidate, count, and percentage variables
    # Winning candidate variable declared with empty STRING tracker (variable = "") since its a name
winning_candidate = ""
winning_count = 0
winning_perc = 0

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
# print(candidate_votes)

# Close the file.
election_data.close()

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_perc = (votes / total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_perc > winning_perc):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_perc = vote_perc
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to terminal.
    print(f"\n{candidate_name}: {vote_perc:.1f}% ({votes:,})\n")

win_sum = (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_perc:.1f}%\n"
    f"----------------------------\n")
print(win_sum)