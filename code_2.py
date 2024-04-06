import csv
import os

# Prompt the user to input the file path
input_path = input("Enter the path to the input CSV file: ")

if not os.path.exists(input_path):
    print("Error: Input file not found.")
    sys.exit(1)

output_text_path = "election_results.txt"

# Variables
total_votes = 0
candidates_votes = {}

# Read data and calculate totals
with open(input_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        # Update the votes for each candidate
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

# Calculate percentage of votes each candidate won
candidates_percentage = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates_votes.items()}

# Find the winner based on popular vote
winner = max(candidates_votes, key=candidates_votes.get)

# Print the results to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate, votes in candidates_votes.items():
    percentage = candidates_percentage[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# text file
with open(output_text_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("----------------------------\n")
    for candidate, votes in candidates_votes.items():
        percentage = candidates_percentage[candidate]
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("----------------------------\n")

print("Results exported to:", output_text_path)

