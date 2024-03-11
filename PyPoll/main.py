import os 
import csv

# import csv using relative path
election_csv = os.path.join("PyPoll","Resources","election_data.csv")


# Lists to store candidates who received votes
candidates = []
candidates_cleaned = []

# variables for candidates
# referenced in candidate cleaned list calculated below
charles_votes = 0
diana_votes = 0
raymon_votes = 0

# open file to read, skip and store header
with open (election_csv, newline="") as file:
    csvreader = csv.reader(file, delimiter = ",")
    header = next (csvreader, None)

# loop through csv file and add candidates to array
    for row in csvreader: 
        candidates.append(row[2])
        
    # count up votes for each candidate (added to code after candidates were determined)
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes += 1

# "set" function used to determine candidates who received votes without repetition
# reference for candidate variables above          
candidates_cleaned = list(set(candidates))
#print(candidates_cleaned)

# calculate percentages and total votes
total_votes = len(candidates)
charles_percentage = round(((charles_votes)/ total_votes) * 100, 3)
diana_percentage = round(((diana_votes)/ total_votes) * 100,3)
raymon_percentage = round(((raymon_votes)/ total_votes) * 100,3)

# determine winner with conditional logic
if charles_percentage > diana_percentage and raymon_percentage:
    winner = "Charles Casper Stockham"
elif diana_percentage > raymon_percentage and charles_percentage:
    winner  = "Diana DeGette"
else: 
    winner = "Raymon Anthony Doane"

#  print to terminal 
print("Election Results \n-------------------")
print(f"Total Votes : {total_votes} \n-------------------"),
print(f"Charles Casper Stockham: {(charles_percentage)}% ({charles_votes})"),
print(f"Diana DeGette: {(diana_percentage)}% ({diana_votes})"),
print(f"Raymon Anthony Doane: {(raymon_percentage)}% ({raymon_votes})"),
print("-------------------"),
print(f"Winner : {winner}")


# create output file and write the results to it
output_file = os.path.join ("PyPoll","analysis","Election_results.csv")

with open (output_file, "w", newline = "") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Election Results"])
    writer.writerow(["---------------------"])
    writer.writerow([f"Total Votes : {total_votes}"])
    writer.writerow(["---------------------"])
    writer.writerow([f"Charles Casper Stockham: {round(charles_percentage,3)}% ({charles_votes})"])
    writer.writerow([f"Diana DeGette: {(diana_percentage)}% ({diana_votes})"])
    writer.writerow([f"Raymon Anthony Doane: {(raymon_percentage)}% ({raymon_votes})"])
    writer.writerow(["---------------------"])
    writer.writerow([f"Winner : {winner}"])




