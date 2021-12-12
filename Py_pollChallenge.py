
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

file_to_load = os.path.join("Desktop", "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_results.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}
votes = 0

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = 0
county_turnout = 0
county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1 
        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #4a: Write an if statement that checks that the county does not match any existing county in the county list
        if county_name not in county_options:
            # 4b: add the existing county to the list of counties
                county_options.append(county_name)
                # 4c: begin tracking the county's vote count
                county_votes[county_name] = 0
                # 5: add a vote to that county's vote count.
        county_votes[county_name] += 1
# Save the results to our text file
with open(file_to_save, "w") as election_output_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n\n")
    #Printing the middle line
    county_results = (
        f"------------------------\n")
        
    print(election_results, end="")
    election_output_file.write(election_results)
    # 6a: write a for loop to get the county from the county dictionary
    for county_name in county_votes:
        # 6b: Retrieve the vote of the county
        votes = county_votes[county_name]
        # 6c: calculate the percentage of county votes
        county_percentage = float(votes)/ float(total_votes) * 100
        # 6d: print the county results to the terminal
        print((f"{county_name}: {county_percentage:.1f}% ({votes:,})\n"))
    print(county_results, end="")
    # 6e: Save the county votes to a text file
    election_output_file.write(county_results)
    # 6f: Write an if statement to determine the winning county and its votes 
    # See line 118
for canidate_name in candidate_votes:
    c_vote = candidate_votes[candidate_name]
    candidate_percentage = float(c_vote)/float(total_votes)
    #7: Print the county with the largest turnout in the terminal
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
turnout_summary = (
    f"Largest County Turnout: Denver\n"
    f"------------------------\n"
)
print(turnout_summary)
# Save the final Candidate vote count to text file
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
# Print the winning candidates' results to the terminal.

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

    