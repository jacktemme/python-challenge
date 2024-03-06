import os 
import csv

election_csv = "PyPoll/Resources/election_data.csv"

charles_votes = 0
diane_votes = 0
raymon_votes = 0
total_votes = 0

with open (election_csv, newline="") as file:
    csvreader = csv.reader(file, delimiter = ",")
    next (csvreader, None)

    for row in csvreader:
        
        total_votes += 1
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        if row[2] == "Diana DeGette":
            diane_votes += 1
        if row[2] == "Raymon Anthony Doane":
            raymon_votes += 1

charles_percentage = ((charles_votes)/ total_votes) * 100
diane_percentage = ((diane_votes)/ total_votes) * 100
raymon_percentage = ((raymon_votes)/ total_votes) * 100

if charles_percentage > diane_percentage and raymon_percentage:
    winner = "Charles Casper Stockham"
if diane_percentage > raymon_percentage and charles_percentage:
    winner  = "Diana DeGette"
if raymon_percentage > diane_percentage and charles_percentage:
    winner = "Raymon Anthony Doane"

print(charles_percentage)
print(diane_percentage)
print(raymon_percentage)





