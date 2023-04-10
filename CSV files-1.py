#Write a Python program to read a given CSV file as a dictionary 
#file name : files-1.csv

import csv

def csv_to_dictionary(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return {row.popitem()[1]: row for row in reader}

 
data = csv_to_dictionary('files-1.csv')
print(data)
