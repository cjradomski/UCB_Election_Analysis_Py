## Add our dependencies
import csv
import os

## Assign variables to load our election results and analysis files.
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

## Initialize a total vote counter.
total_votes = 0

## Candidate options, county, and candidate votes
candidate_options = []
counties = []
## Declare empty dictionaries for candidate votes and counties
candidate_votes = {}
counties_dict = {}

## Intialize variables to determine winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

## Initialize variables to determine coutnies with the largest turnout
most_votes_county = ""
most_votes_county_count = 0
most_votes_county_percentage = 0

## Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    ## Loop through rows
    for row in file_reader:
        ## Add to the total vote count.
        total_votes += 1

        ## Print the candidate and county name from each row
        candidate_name = row[2]

        county_name = row[1]

        ## If statement to count candidates' votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        ## If statement to count counties' votes
        if county_name not in counties:
            counties.append(county_name)
            counties_dict[county_name] = 0

        counties_dict[county_name] += 1

    ## Save results to analysis text file
    with open(file_to_save, "w") as txt_file:

        ## Printing Total Votes to Terminal and text file
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        
        txt_file.write(election_results)
        
        ## Printing County Vote to Terminal and text file
        print("\nCounty Votes:\n")
        txt_file.write("\nCounty Votes:\n")

        ## Loop through counties and find percentage of votes in county
        for county in counties_dict:    
            county_votes = counties_dict[county]
            county_vote_percentage = float(county_votes) / float(total_votes) * 100

            turnout_results = (f"{county}: {county_vote_percentage:.1f}% ({county_votes:,})\n")

            print(turnout_results)

            txt_file.write(turnout_results)

        ## If to determine county with the most votes
            if (county_votes > most_votes_county_count) and (county_vote_percentage > most_votes_county_percentage):
                most_votes_county_count = county_votes
                most_votes_county_percentage = county_vote_percentage

                most_votes_county = county

        ## Print county with largest turnout
        largest_county_turnout = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {most_votes_county}\n"
            f"-------------------------\n")
        print(largest_county_turnout)

        txt_file.write(largest_county_turnout)

        ## Printing Candidate Vote to Terminal and text file
        ## Loop through candidates and find percentage of votes for each candidate
        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)
            txt_file.write(candidate_results)

            ## If to determine candidate with most votes
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate  

        ## Print the winning candidate's results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        txt_file.write(winning_candidate_summary)
                
