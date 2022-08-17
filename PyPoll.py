# The data we need to retrieve:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable for the file to load from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize a total vote counter
total_votes = 0

# Declare a new list to hold candidate info
candidate_options = []
# Declare an empty dictionary to hold vote counts for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's vote count.
        candidate_votes[candidate_name] += 1


    # Use the open statement to open the file as a text file.
    with open(file_to_save, 'w') as txt_file:
        # Write some data to the file.
        txt_file.write("Counties in the Election\n")
        txt_file.write("------------------------\n")
        txt_file.write("Arapahoe\nDenver\nJefferson\n")

    # Close the file
    txt_file.close()

# Close the file.
election_data.close()

# Determine the percentage of votes for each candidate by looping through the counts.
# Interate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # TODO: print out each candiate's name, vote count, and percentage of
    # votes to the terminal
    print(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning_count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and
        # winning_percentage = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"------------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------------------------\n"
)
print(winning_candidate_summary)