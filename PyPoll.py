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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyize data
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    

# Close the file.
election_data.close()