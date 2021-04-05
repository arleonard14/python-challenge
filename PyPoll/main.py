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

   for row in csvreader:
     # print number of votes
        votes+=1

        if row[2] not in candidate:
           candidate.append(row[2])


print(f"Total Votes: {votes}")
print(f"Candidates: {candidate}")