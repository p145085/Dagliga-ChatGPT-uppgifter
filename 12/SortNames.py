#12. Skapa ett program som sorterar en lista med namn från en fil.
def sort_names_from_file(filename):
    # Open the file and read the names
    with open(filename, 'r') as file:
        names = file.readlines()

    # Clean up names (strip newline characters)
    names = [name.strip() for name in names]

    # Sort the names alphabetically
    names.sort()

    # Return the sorted list
    return names

# Example usage
filename = 'names.txt'
sorted_names = sort_names_from_file(filename)
print("\n".join(sorted_names))
