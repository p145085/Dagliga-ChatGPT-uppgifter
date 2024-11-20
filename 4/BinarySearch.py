#4. Implementera en sökfunktion i en sorterad lista (binärsökning).
def binary_search_recursive(sorted_list, target, low, high):
    if low > high:
        return -1  # Basfall: målet finns inte i listan

    mid = (low + high) // 2
    if sorted_list[mid] == target:
        return mid
    elif sorted_list[mid] < target:
        return binary_search_recursive(sorted_list, target, mid + 1, high)
    else:
        return binary_search_recursive(sorted_list, target, low, mid - 1)

# Exempelanvändning
my_list = [1, 3, 5, 7, 9, 11]
target = 7
print(binary_search_recursive(my_list, target, 0, len(my_list) - 1))  # Output: 3
