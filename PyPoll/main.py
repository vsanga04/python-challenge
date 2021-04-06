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
    
    csvheader = next(csvfile)
    
    Candidate_Names = []
    for row in csvfile:
        Candidate_Names.append(row[2])

    Candidate_set = list(set(Candidate_Names))
    print(Candidate_set)



 
 
# The total number of votes each candidate won
    # OTooley_votes = Candidate_Names.count("O'Tooley")
    # print(OTooley_votes)
    # Li_votes = Candidate_Names.count("Li")
    # print(Li_votes)
    # Khan_votes = Candidate_Names.count("Khan")
    # print(Khan_votes)
    # Correy_votes = Candidate_Names.count("Correy")
    # print(Correy_votes)
    # Candidates = []
    # Candidate_Votes = []
  

    #https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
    Candidate_Count = {}
    [Candidate_Count.update({i:Candidate_Count.get(i,0)+1}) for i in Candidate_Names]
    print(Candidate_Count)

    #for x in range(Candidate_set):
# The percentage of votes each candidate won 
   # OTooley_Percent = OTooley_votes/total_votes
   # print(OTooley_Percent)
   #https://www.tutorialfor.com/questions-133100.htm
    Percentages = {}
    for i in Candidate_Count:
        Percentages[i] = "{:.2%}".format(Candidate_Count[i]/total_votes)
    print(Percentages)

# The winner of the election based on popular vote.
    winner = max(Candidate_Count, key=Candidate_Count.get)
    print("Winner of the election is " + winner)

# your final script should both print the analysis to the terminal and export a text file with the results.
