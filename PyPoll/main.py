## PyPoll - import csv
import os
import csv

# read csv
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    print(csvfile)



#dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# create a Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast



# A complete list of candidates who received votes

# The percentage of votes each candidate won
 
 
# The total number of votes each candidate won
 

# The winner of the election based on popular vote.
 
# your final script should both print the analysis to the terminal and export a text file with the results.
