#PyBank
import os
import csv

# Path to CSV file
PyBankcsv = os.path.join("Resources","budget_data.csv")

#Create List
date = []
monthly_changes = []
profit_loss = []

# Declare Variable
mcount = 0
net_profit = 0
total_change_profits = 0
start_profit = 0

#Open and read csv file
with open(PyBankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Read through each row
    #for row in csv_header:
    for row in csvreader:
        #Count how many month'
        mcount = mcount + 1

        #Add data and revenue to list)
        date.append(row[0])
        profit_loss.append(row[1])

        #count total revenue
        net_profit = net_profit + int(row[1])

        #Average Change and store
        end_profit = int(row[1])
        monthly_change_profits = end_profit - start_profit
        monthly_changes.append(monthly_change_profits)

        #Calculate the average change
        total_change_profits = total_change_profits + monthly_change_profits
        average_change_profits = (total_change_profits / mcount)
        start_profit = end_profit

        #Compare dates with change in profits
        greatest_increase_profits = max(monthly_changes)
        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        greatest_decrease_profits = min(monthly_changes)
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

    #Print to screen
    print("--------------------------")
    print("Financial Analysis")
    print("--------------------------")
    print("Total Months: " + str(mcount))
    print("Total Profits: " + "$" + str(net_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")
    print("--------------------------")

#Print to file
with open('financial_analysis.txt', 'w') as text:
    text.write("--------------------------\n")
    text.write("Financial Analysis"+ "\n")
    text.write("--------------------------\n\n")
    text.write("Total Months: " + str(mcount) + "\n")
    text.write("Total Profits: " + "$" + str(net_profit) +"\n")
    text.write("Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("--------------------------\n")
