"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


callers=[]
recievers=[]
texts_senders=[]
texts_recievers=[]
possible_telemarketers=[]


for row in calls:
    callers.append(row[0])
    recievers.append(row[1])

for row in texts:
    texts_senders.append(row[0])
    texts_recievers.append(row[1])
    
for number in callers:
    if (number not in recievers)&(number not in texts_senders)&(number not in texts_recievers)&(number not in possible_telemarketers):
        possible_telemarketers.append(number)

possible_telemarketers.sort()
print("These numbers could be telemarketers: ")
for number in possible_telemarketers:
        print(number)
