#import os module
import os
#Module for reading CSV file
import csv

csvpath=os.path.join('python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

#read CSV file
with open(csvpath) as csvfile:
   #CSV reader specifies delimeter and variable
   csvreader=csv.reader(csvfile, delimiter=',')

   print(csvreader)

   # Read header row first
   csv_header=next(csvreader)
   # print(f"CSV Header: {csv_header}")
   
   votes=0
   candidate=[]
   Li=0
   Correy=0
   Khan=0
   OTooley=0

   for row in csvreader:
     # number of votes
        votes+=1

      # list of candidates and totals
        if row[2] not in candidate:
           candidate.append(row[2])

        if "Khan" in row:
            Khan+=1
        if "Correy" in row:
            Correy+=1
        if "Li" in row:
            Li+=1
        if "O'Tooley" in row:
            OTooley+=1
      
print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {votes}")
print(f"--------------------------")
print(f"Khan: {round((Khan/votes)*100)}% ({Khan})")
print(f"Correy: {round((Correy/votes)*100)}% ({Correy})")
print(f"Li: {round((Li/votes)*100)}% ({Li})")
print(f"O'Tooley: {round((OTooley/votes)*100)}% ({OTooley})")
print(f"--------------------------")
print(f"Winner: Khan")