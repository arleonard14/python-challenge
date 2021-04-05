#import os module
import os
#Module for reading CSV file
import csv

csvpath=os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

#read CSV file
with open(csvpath) as csvfile:
   #CSV reader specifies delimeter and variable
   csvreader=csv.reader(csvfile, delimiter=',')

   print(csvreader)

   # Read header row first
   csv_header=next(csvreader)
   # print(f"CSV Header: {csv_header}")

   months=0
   total=0.0
   prev_total=0
   profit_loss=[]
   pl_months=[]

   # Read each row of data after header
   for row in csvreader:
      # find total
      total+=int(row [1])

   # If not the first row
      if months != 0:
         temp_pl= int(row[1])-int(prev_total)
         profit_loss.append(temp_pl)

   # Add to next row    
      else:
         profit_loss.append(0)
       
      pl_months.append(row[0])

      # add to number of months
      months+=1
      prev_total=int(row[1])

# Find Average Change
   average_change=sum(profit_loss)/(months-1)

# Find Greatest Increase
   max_pl_num=max(profit_loss)
   max_pl_idx=profit_loss.index(max_pl_num)
   max_pl_month=pl_months[max_pl_idx]

# Find Greatest Decrease
   min_pl_num=min(profit_loss)
   min_pl_idx=profit_loss.index(min_pl_num)
   min_pl_month=pl_months[min_pl_idx]

# Define lists
months_total=[months]
total_list=[total]
average_change_list=[average_change]
increase_list_month=[max_pl_month]
decrease_list_month=[min_pl_month]
increase_list=[max_pl_num]
decrease_list=[min_pl_num]

# export to csv
cleaned_csv = zip(months_total, total_list, average_change_list, increase_list_month, increase_list, decrease_list_month, decrease_list)
output_file = os.path.join("output_pybank.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Months", "Total", "Average Change", "Greatest Increase Month", "Greatest Increase", "Greatest Decrease Month","Greatest Decrease"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
   
 # print total
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {months}")
print(f"Total: {total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_pl_month} ${max_pl_num}")
print(f"Greatest Loss in profits: {min_pl_month} ${min_pl_num}")

   
