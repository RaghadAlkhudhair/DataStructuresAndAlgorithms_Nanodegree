"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
    numbers=[]
    
    for i in range(len(texts)):
        numbers.append(texts[i][0])
        numbers.append(texts[i][1])


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)   

    for i in range(len(calls)):
        numbers.append(calls[i][0])
        numbers.append(calls[i][1])
        
    print("There are "+ str(len(set(numbers))) +" different telephone numbers in the records")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""