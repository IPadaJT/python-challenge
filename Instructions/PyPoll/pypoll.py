# #You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

import os
import csv #same start as pybank
election_data=os.path.join("Resources","election_data.csv")

vote_total=0 
#Set up a dictionary to hold votes per candidate
votesbycand={}

#Access file to be read
with open(election_data, 'r', encoding="utf8") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader) #Eat the header
    # print (f"{csv_header}") to check that the header is being 'ate'
    for row in csvreader:
        vote_total += 1
        if row[2] not in votesbycand:
            votesbycand[row[2]]=1
        else: 
            votesbycand[row[2]]+=1
    #For each row of data following the header, add +1 to vote total and count votes per candidate.

    # print (f"{vote_total} and the votes per candidate: {votesbycand}")
    # Check work here



#Print Results
print("Election Results")
print(f"Total Votes: {vote_total}")
for candidate, votes in votesbycand.items():
    print(candidate + ":" + "{:.2%}".format(votes/vote_total)+ " ("+str(votes) +")")
    #This for statement looks at votes by candidate and prints individual results rounded to 2 decimal places using {.2%}
mayor=max(votesbycand, key=votesbycand.get)
print(f"Winner: {mayor}")

#Write to output file
output_path=os.path.join("Analysis", "analysis.txt")

with open(output_path, 'w') as analysis:
    analysis.write("Election Results\n")
    analysis.write(f"Total Votes: {vote_total} \n")
    for candidate, votes in votesbycand.items():
        analysis.write(candidate + ":" + "{:.2%}".format(votes/vote_total)+ " ("+str(votes) +")"+"\n")
    analysis.write(f"Winner: {mayor} \n")
