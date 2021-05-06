import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a txt file
with open(file_to_load) as election_data:

    # To do: read and analyze the data
    file_reader = csv.reader(election_data)

    # Print header
    headers = next(file_reader)
    print(headers)


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

