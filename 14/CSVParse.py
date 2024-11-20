#14. Skapa en CSV-parser och exportera data till CSV-format.

import csv

# Data to be written into the CSV file (list of lists)
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Writing data to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write multiple rows


#################################################

import csv

# Reading data from the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#################################################

import csv

# Data to write
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]

# Writing data with headers to CSV
with open('data_with_headers.csv', 'w', newline='') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write headers
    writer.writerows(data)

#################################################

import csv

# Reading data with headers as dictionary
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is a dictionary  
