#11. Läs en textfil och räkna antalet rader.

def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

# Test the function with a file
filename = "example.txt"
print(f"Number of lines: {count_lines_in_file(filename)}")


############################################################

#I bash är det superenkelt:
#wc -l example.txt
