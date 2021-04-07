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
#sum of column: https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python
with open(csvpath) as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    #print(csvfile)
    csvheader = next(csvfile)     
    Total_PL = []
    for row in csvfile:
        Total_PL.append(float(row[1]))
    print(sum(Total_PL))

    # Total_PL  = 0
    # for row in csvfile:
    #     Total_PL += int(row[1])
    # print(Total_PL)

    
#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in

with open(csvpath) as csvfile:
    csvfile = csv.reader(csvfile, delimiter=',')
    #print(csvfile)
    csvheader = next(csvfile)  
    rev_change = []
    for i in range(1,len(Total_PL)):
        rev_change.append(Total_PL[i] - Total_PL[i-1])
        avg_RevChange = round(sum(rev_change)/len(rev_change),2)
    print(avg_RevChange)

#   * The greatest increase in profits (date and amount) over the entire period
    Greatest_Inc = max(rev_change)
    Greatest_Inc_Date = str(Date[rev_change.index(max(rev_change))])
    print(Greatest_Inc_Date, Greatest_Inc)
#   * The greatest decrease in losses (date and amount) over the entire period
    Greatest_Dec = min(rev_change)
    Greatest_Dec_Date = str(Date[rev_change.index(min(rev_change))])
    print(Greatest_Dec_Date, Greatest_Dec)
    
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
csvfile2 = os.path.join("Analysis", "budget_analysis.txt")
with open(csvfile2, "w") as budget_analysis:
    budget_analysis.write(f'Total Months: {total_months}')
    budget_analysis.write("==============================")
    budget_analysis.write(f"The average net change: {avg_RevChange}")
    budget_analysis.write("==============================")
    budget_analysis.write(f"The greatest increase in profits, date and amount: {Greatest_Inc_Date}, :, {Greatest_Inc}")
    budget_analysis.write("==============================")
    budget_analysis.write(f"The greatest decrease in profits, date and amount: {Greatest_Inc_Date}, :, {Greatest_Inc}")