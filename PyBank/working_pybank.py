# In this Challenge, you are tasked with creating a Python script
# to analyze the financial records of your company. You will be
# given a financial dataset called budget_data.csv. The dataset
# is composed of two columns: "Date" and "Profit/Losses".

# Your task is to create a Python script that analyzes the records
# to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then
# the average of those changes

# The greatest increase in profits (date and amount) over the
# entire period

# The greatest decrease in profits (date and amount) over the
# entire period

import os
import csv

# Make variables to analyze the dataset

rowCount = 0
netTotal = 0
lastProfLoss = 0
currentProfLoss = 0
totalAverage = 0
greatestGain = 0
greatestGainDate = ""
greatestDecrease = 0
greatestDecreaseDate = ""


# connect my python file to the csv file using the path join function, set csv to read and store headers to skip them in the for loop

budget_data = os.path.join("Resources", "budget_data.csv")
with open(budget_data) as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)

# for loop to perform the calculations needed for final figures
    for row in reader:
        # use the row count variable to calculate number of months in the data set
        rowCount += 1
        # use the net total variable to calculate the total profit and loss for the data set
        netTotal += float(row[1])
        # set up loop to get averages and greatest profit and loss
        currentProfLoss = float(row[1]) - lastProfLoss
        if rowCount > 1:
            totalAverage += currentProfLoss
        # update figures
        lastProfLoss = float(row[1])
        # get the greatest gain values
        if currentProfLoss > greatestGain:
            greatestGain = currentProfLoss
            greatestGainDate = row[0]
        # get the greatest decrease values
        elif currentProfLoss < greatestDecrease:
            greatestDecrease = currentProfLoss
            greatestDecreaseDate = row[0]


# Print all the data gathered into the format provided to follow

print("Financial Analysis \n----------------------------")
print(f"Total Months: {rowCount}"),
print(f"Total: ${netTotal:.0f}"),
print(f"Average Change: ${(totalAverage / (rowCount - 1)):.2f}"),
print(f"Greatest Increase in Profits: {greatestGainDate} (${greatestGain:.0f})"),
print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease:.0f})")

