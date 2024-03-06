import os
import csv

# import csv using relative path
budget_csv = "PyBank/Resources/budget_data.csv"

# set up variables for iterations
months = []
profits = []
profit_change = []
total_amount = 0

# open file to read
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader, None)

# loop through csv file and otput the month and profit/losses
    for row in csvreader:
        total_amount = total_amount + int(row[1])
        months.append(row[0])
        profits.append(row[1])

# from profit list determine profit changes over time
for x in range(1, len(profits)):
    profit_change.append((int((profits[x])) - (int(profits[x-1]))))

# calculate total months and average, max, and min values of profit changes
month_count = len(months)
average_change = sum(profit_change) / len(profit_change)
max_change = max(profit_change)
min_change = min(profit_change)

# find index for max and min change to reference the date it occured
date_index = profit_change.index(max_change)
date_index1 = profit_change.index(min_change) 

# print findings to terminal
print("Financial Analysis\n-----------------")       
print(f"Total Months: {month_count}")
print(f"Total: ${total_amount}")
print(f"Average: ${round(average_change, 2)}")
print(f"Greatest Increase in profits: {months[date_index + 1]} (${max_change})")
print(f"Greatest Decrease in profits: {months[date_index1 + 1]} (${min_change})")

# create a csv file to write results to
out_file = os.path.join("PyBank/analysis/Profit_Results.csv")

with open (out_file,"w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------"]) 
    writer.writerow([f"Total Months: {month_count}"])
    writer.writerow([f"Total: ${total_amount}"])
    writer.writerow([f"Average: ${round(average_change, 2)}"])
    writer.writerow([f"Greatest Increase in profits: {months[date_index + 1]} (${max_change})"])
    writer.writerow([f"Greatest Decrease in profits: {months[date_index1 + 1]} (${min_change})"])
