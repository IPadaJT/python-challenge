# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)


#Read csv file
import os
import csv #These 2 imports allow me to read/write csv files and create pathways to do so
import statistics #This might make the math easier

#Here I'll define some variables to hold the various things we're trying to analyze
month_count=0
cash_total=0
great_profit=0
worst_dec=0
great_month=""
worst_month=""
change=[]
monthlychange=[]

budget_data_csv=os.path.join("Resources", "budget_data.csv")
with open(budget_data_csv, 'r', encoding="utf8") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",") # This tells it to read the csv file and split things by the commas
    csv_header= next(csvreader) 
    #This reads the header row. Double check by printing print(f"CSV Header: {csv_header}"")
    for row in csvreader: #Here I can check that it's being read properly by print(row)
        month_count += 1 
        cash_total += int(row[1]) 
        #Found on stackoverflow += is the same idea as saying sum=0, sum=sum+x to get a total 

        if int(row[1])>great_profit:
            great_month=row[0]
            great_profit=int(row[1])
            # This block of code says run through the rows 
            # and if it's greater than the current stored great profit. 
            # Replace the current with the new and mark the month
        elif int(row[1])<worst_dec:
            worst_month=row[0]
            worst_dec=int(row[1])
            #Same logic as with good month
        change.append(int(row[1]))

for x in range(len(change)-1): 
    monthlychanges=(change[x+1]-change[x])
    monthlychange.append(monthlychanges)
    #This block counts the changes over the months

#To find the average change, I will just use the statistics module
average_change=statistics.mean(monthlychange)

#Check by printing results
print ("Financial Analysis")
print(f"-------------")
print(f"Total Months: " + str(month_count))
print(f"Total: " + str(average_change))
print(f"Average Change: " + str(cash_total))
print(f"Greatest increase: " + str(great_month) + " " + str(great_profit))
print(f"Greatest decrease: " + str(worst_month) + " " + str(worst_dec))

#Now output to a CSV file
output_path=os.path.join("Analysis", "analysis.txt")

with open(output_path, "w") as analysis:
    #csvwriter=csv.writer(analysis, delimiter=',')
    analysis.write("Financial Analysis\n")
    analysis.write("-------------\n")
    analysis.write(f"Total Months: " + str(month_count)+"\n")
    analysis.write(f"Total: " + str(average_change)+"\n")
    analysis.write(f"Average Change: " + str(cash_total)+"\n")
    analysis.write(f"Greatest increase: " + str(great_month) + " " + str(great_profit)+"\n")
    analysis.write(f"Greatest decrease: " + str(worst_month)+ " " + str(worst_dec)+"\n")