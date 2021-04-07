import os
import csv

# read and parse csv
csvpath = os.path.join("Resources", "budget_data.csv")



with open(csvpath) as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    #print(csvfile)

    csvheader = next(csvfile)
    #print(f"{csvheader}")

# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset
    Date = [(row[0]) for row in csvfile]
    total_months = len(Date)
    print(f'Total Months: {total_months}')

#   * The net total amount of "Profit/Losses" over the entire period
    # Total_PL = []
    # for row in csvfile:
    #     Total_PL.append(row[1])
    # print(sum(Total_PL)) 

#sum of column: https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python
with open(csvpath) as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    #print(csvfile)
    csvheader = next(csvfile)      
    Total_PL  = 0
    for row in csvfile:
        Total_PL += int(row[1])
    print(Total_PL)

    
#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for i in range(1,len(Total_PL)):
        rev_change.append(Total_PL(i) - revenue[i-1])
    print(rev_change)

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.