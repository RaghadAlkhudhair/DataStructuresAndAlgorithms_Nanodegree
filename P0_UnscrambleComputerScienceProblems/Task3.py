"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

Bangalore_calls_recievers=[]
Bangalore_calls_recievers_Bangalore=[]
num_of_calls=0
num_of_calls_in_Bangalore=0

for row in calls:
    if row[0][0:5]=='(080)':  ## If the caller is from Bangalore

            
        if (row[1][0:5]=='(080)'):
            num_of_calls_in_Bangalore+=1
          
        if (row[1][0:2]=='(0'):
            num_of_calls+=1
            if((row[1][0:(row[1].index(')')+1)]) not in Bangalore_calls_recievers):
                Bangalore_calls_recievers.append(row[1][0:(row[1].index(')')+1)])
            
            
            
        if ((' ' in row[1]) & (row[1][0]=='7' or row[1][0]=='8' or row[1][0]=='9')):
            num_of_calls+=1
            if((row[1][0:4]) not in Bangalore_calls_recievers):
                Bangalore_calls_recievers.append(row[1][0:4])

            
            
        if(row[1][0:2]=='140'):
            num_of_calls+=1
            if((row[1][0:3]) not in Bangalore_calls_recievers):
                Bangalore_calls_recievers.append(row[1][0:3])

            

Bangalore_calls_recievers.sort()

print("\n The numbers called by people in Bangalore have codes: ") 
for num in Bangalore_calls_recievers:
    print(str(num))

print("\n"+str(round( num_of_calls_in_Bangalore/num_of_calls*100,2)) +" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
