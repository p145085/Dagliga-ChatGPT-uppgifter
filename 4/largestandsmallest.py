# **Hitta det största och minsta talet i en lista:** Skriv ett program som returnerar det största och minsta talet från en given lista.
def find_max_min(numbers):
    # Kolla om listan är tom
    if not numbers:
        return None, None
    
    # Hitta det största och minsta talet
    max_num = max(numbers)
    min_num = min(numbers)
    
    return max_num, min_num

# Exempel på användning
numbers = [3, 5, 7, 2, 8, -1, 4]
max_num, min_num = find_max_min(numbers)

print("Största talet:", max_num)
print("Minsta talet:", min_num)
