import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Initialize Winning Candidate and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Using the with statement open the file as a txt file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header
    headers = next(file_reader)
    
    # Add up the votes
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        # If candidate is not in the list
        if candidate_name not in candidate_options:

            # Add candidate to the list
            candidate_options.append(candidate_name)

            # Initialize candidate's votes
            candidate_votes[candidate_name] = 0

        # Add a vote to candidate's votes
        candidate_votes[candidate_name] +=1

# Determine percentage votes
for candidate_name in candidate_votes:
    # Retrieve vote count
    votes = candidate_votes[candidate_name]
    # Calculate vote percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes})\n")
    # Determine winner and winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, set winning count and winning percentage = to that candidate's values
        winning_count = votes
        winning_percentage = vote_percentage
        # Set winning_candidate equal to winner's name
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"--------------------------\n")
print(winning_candidate_summary)
