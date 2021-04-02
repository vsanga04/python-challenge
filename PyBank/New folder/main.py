import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open and read csv
#with open(budget_data_csv) as csv_file:
 #   csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")


    for row in csvreader:

        # Convert row to float and compare to grams of fiber
        if float(row[1]) >= 5:
            print(row)
