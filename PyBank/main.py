import os
import csv

budget_csv = os.path.join("/Users/jacktemme/Desktop/python-challenge/PyBank/Resources/budget_data.csv")


months = []
profits = []
total_amount = 0
firstline = True

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        if firstline:
            firstline = False
        else:
            total_amount = total_amount + int(row[1])
            months.append(row[0])
            profits.append(row[1])

  
month_count = len(months)

profit_change = []

for x in range(1, len(profits)):
    profit_change.append((int((profits[x])) - (int(profits[x-1]))))


average_change = sum(profit_change) / len(profit_change)
max_change = max(profit_change)
min_change = min(profit_change)

date_index = profit_change.index(max_change)
date_index1 = profit_change.index(min_change) 

print("Financial Analysis\n-----------------")       
print(f"Total Months: {month_count}")
print(f"Total: ${total_amount}")
print(f"Average: {round(average_change, 2)}")
print(f"Greatest Increase in profits: {months[date_index + 1]} (${max_change})")
print(f"Greatest Decrease in profits: {months[date_index1 + 1]} (${min_change})")

