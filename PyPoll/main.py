## PyPoll - import csv

import os
import csv

# read and parse csv
csvpath = os.path.join("Resources", "election_data.csv")



with open(csvpath) as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    print(csvfile)

    csvheader = next(csvfile)
    print(f"{csvheader}")

#dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
    VoterId = [int(row[0]) for row in csvfile]
    total_votes = len(VoterId)
    print(total_votes)
   

# A complete list of candidates who received votes

with open(csvpath) as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    Candidate_Names = []
    for row in csvfile:
        Candidate_Names.append(row[2])

    Candidate_set = set(Candidate_Names)
    print(Candidate_set)
#        Candidates_column = row[2]
 #       if Candidates in Candidate_column:
  #              candidate_index = Candidates.index(Candidates)

# The percentage of votes each candidate won
 
 
# The total number of votes each candidate won
 

# The winner of the election based on popular vote.
 
# your final script should both print the analysis to the terminal and export a text file with the results.
