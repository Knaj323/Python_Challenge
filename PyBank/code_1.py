import csv
import os

# File paths
input_path = "/Users/khalidnaji/Desktop/Mod #3/budget_data.csv"
output_text_path = "financial_analysis.txt"

# Variables
total_months = 0
total_profit = 0
previous_profit = 0
profit_changes = []
dates = []

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
        dates.append(row[0])  # Assuming date is in the first column
        previous_profit = profit

# Calculate average profit
average_change = sum(profit_changes) / (total_months - 1)  # Exclude the first month from the average

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

# text file
with open(output_text_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total Profits: ${total_profit}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Results exported to:", output_text_path)






         