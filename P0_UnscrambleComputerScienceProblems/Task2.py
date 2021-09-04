
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

numbers=[]

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
for i in range(len(calls)):
    numbers.append(calls[i][0])
    numbers.append(calls[i][1])
    
numbers=set(numbers)
longest_time_number=''
max_time=0
    
for number in numbers:
    time=0
    for record in calls:
        if (number==record[0] or number==record[1]):
            time+=int(record[3])
    if time>max_time:
        max_time=time
        longest_time_number=number
            
print(longest_time_number+" spent the longest time, "+str(max_time)+
          " seconds, on the phone during September 2016")
    

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
