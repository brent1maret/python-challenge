# import and read data

import os
import csv

budget = os.path.join("PyBank\Resources\\budget_data.csv")
#print(budget)

with open(budget, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    profit_loss = []
    profit_loss_total= []
    total_months = []
    average_change = []
    max_profit = []
    min_profit = []
    max_date = []
    min_date = []

#The net total amount of "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
    for row in csvreader:
        revenue = int(row[1])
        profit_loss.append(revenue)
        profit_loss_total = round(sum(profit_loss))
        max_profit = round(max(profit_loss))
        min_profit = round(min(profit_loss))



# he total number of months included in the dataset
total_months = len(list(budget))


#The average of the changes in "Profit/Losses" over the entire period
average_change = round(total_months / profit_loss_total)



print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_loss_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: ${max_profit}")
print(f"Greatest Decrease in Profits: ${min_profit}")

#Output to text file
	text_file = open("pybank.txt", "w")
	text_file.write("Financial Analysis")
	text_file.write("------------------------\n")
	text_file.write("Total months: " + {total_months} + "\n")
	text_file.write("Total volume: " + {profit_loss_total} + "\n")
	text_file.write("Average monthly change: " + {average_change} + "\n")
	text_file.write("Greatest increase in Profits: " + {max_profit} + "\n")
	text_file.write("Greatest decrease in Profits: " + {min_profit}+ "\n")
	text_file.close()
