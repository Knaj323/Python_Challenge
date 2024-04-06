import csv
import os

# Variables
total_months = 0
total_profit = 0
previous_profit = 0
profit_changes = []
dates = []

# Prompt the user to input the file path
input_path = input("Enter the path to the input CSV file: ")

if not os.path.exists(input_path):
    print("Error: Input file not found.")
    sys.exit(1)

# Print data and calculate totals
with open(input_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        total_months += 1
        profit = int(row[1])
        total_profit += profit
        profit_change = profit - previous_profit
        profit_changes.append(profit_change)
        dates.append(row[0])
        previous_profit = profit

# Calculate average profit
average_change = sum(profit_changes) / (total_months - 1)

# Find the highest increase and decrease in profits
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Get the corresponding dates for the greatest increase and decrease
greatest_increase_date = dates[profit_changes.index(greatest_increase)]
greatest_decrease_date = dates[profit_changes.index(greatest_decrease)]

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profits: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")






         
