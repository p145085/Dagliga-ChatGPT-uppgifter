#13. Läs och skriv JSON-data till en fil.

import json

# Python dictionary to be converted to JSON
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Writing JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)


##############################################

import json

# Reading JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Printing the Python object (dictionary)
print(data)
