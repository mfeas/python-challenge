# In this Challenge, you are tasked with helping a small, rural
# town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv.
# The dataset is composed of three columns: "Voter ID", "County",
# and "Candidate". Your task is to create a Python script that
# analyzes the votes and calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

import os
import csv

# Make variables to analyze the dataset


totalVotes = 0
stockham = "Charles Casper Stockham"
stockhamVotes = 0
degette = "Diana DeGette"
degetteVotes = 0
doane = "Raymon Anthony Doane"
doaneVotes = 0
popularVote = ""

# connect my python file to the csv file using the path join function, set csv to read and store headers to skip them in the for loop

election_data = os.path.join("Resources", "election_data.csv")
with open(election_data) as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)

# make variable to track total votes

    for row in reader:
        totalVotes += 1
        if row[2] == stockham:
            stockhamVotes += 1
        elif row[2] == degette:
            degetteVotes += 1
        else:
            doaneVotes += 1

# get the percentages of all the canidates votes

stockhamPercentage = stockhamVotes / totalVotes
degettePercentage = degetteVotes / totalVotes
doanePercentage = doaneVotes / totalVotes


# use all the data gathered from the python script to find the popular vote

if stockhamVotes > degetteVotes and stockhamVotes > doaneVotes:
    popularVote = stockham
elif degetteVotes > stockhamVotes and degetteVotes > doaneVotes:
    popularVote = degette
else:
    popularVote = doane


# Print all the data gathered into the format provided to follow

print("Election Results \n-------------------------"),
print(f"Total Votes: {totalVotes} \n-------------------------"),
print(f"Charles Casper Stockham: {stockhamPercentage:.3%} ({stockhamVotes})"),
print(f"Diana DeGette: {degettePercentage:.3%} ({degetteVotes})"),
print(
    f"Raymon Anthony Doane: {doanePercentage: .3%} ({doaneVotes}) \n-------------------------"),
print(f"Winner: {popularVote}\n-------------------------")

# Make and write into the analysis text file

with open('analysis.txt', 'w') as f:

    f.write("Election Results \n-------------------------\n"),
    f.write(f"Total Votes: {totalVotes} \n-------------------------\n"),
    f.write(
        f"Charles Casper Stockham: {stockhamPercentage:.3%} ({stockhamVotes})\n"),
    f.write(f"Diana DeGette: {degettePercentage:.3%} ({degetteVotes})\n"),
    f.write(
        f"Raymon Anthony Doane: {doanePercentage: .3%} ({doaneVotes}) \n-------------------------\n"),
    f.write(f"Winner: {popularVote}\n-------------------------")
