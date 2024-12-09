# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
previous_month_profit = 0
greatest_increase = ["", 0]  # [Month, Amount]
greatest_decrease = ["", 0]  # [Month, Amount]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        # Track the total months
        total_months += 1

        # Track the total net amount
        total_net += int(row[1])

        # Skip the first row for net change, as there's no previous month to compare
        if total_months == 1:
            previous_month_profit = int(row[1])
            continue

        # Calculate the change in profit/losses (net_change)
        net_change = int(row[1]) - previous_month_profit
        net_change_list.append(net_change)

        # Check for greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]

        # Check for greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

        # Update previous_month_profit for the next iteration
        previous_month_profit = int(row[1])

# Calculate the average net change
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output to the terminal
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)