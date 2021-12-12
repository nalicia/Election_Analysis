
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

file_to_load = os.path.join("Desktop", "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
total_county_votes = 0
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
        total_county_votes += 1
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
        #4a: Write an if stement that checks that the county does not match any existing county in the county list
        if county_name not in county_options:
            # 4b: add the existing county to the list of counties
                county_options.append(county_name)
                # 4c: begin tracking the county's vote count
                county_votes[county_name] = 0
                # 5: add a vote to that county's vote count.
        county_votes[county_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
       f"\nElection Results\n"
       f"-------------------------\n"
       f"Total Votes: {total_votes:,}\n"
       f"-------------------------\n\n"
       f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results, end="")
    # 6a: write a for loop to get the county from the county dictionary
    for county_options in county_votes:
        # 6b: Retrieve the vote of the county
        votes = county_votes[county_name]
        # 6c: calculate the percentage of county votes
        county_percentage = float(votes)/float(total_votes) * 100
        # 6d: print the county results to the terminal
    
with open(file_to_save, "w") as txt_file:
    county_results = (
        f"\n County Results\n"
        f"----------------------\n"
        f"County Votes:{total_county_votes:,}\n"
        f"----------------------\n"
        f"County Votes:\n")
    print(county_results, end="")
    txt_file.write(county_results)

    if (votes > winning_count) and (county_percentage > county_percentage):
        winning_count = votes
        winning_percentage = county_percentage
        winning_candidate = candidate_name
    print((f"{county_name}: {county_percentage:.1f}% ({votes:,})\n"))
 
    