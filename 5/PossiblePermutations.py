#5. **Implementera en funktion som returnerar alla möjliga permuteringar av en given lista.**

def get_permutations_recursive(lst):
    # Base case: if list has only one element, return it as a single permutation
    if len(lst) <= 1:
        return [lst]
    
    permutations = []
    # Take each element as first element and permute the rest
    for i in range(len(lst)):
        current = lst[i]
        # Remove current element from list
        remaining = lst[:i] + lst[i+1:]
        
        # Recursively get permutations of remaining elements
        for p in get_permutations_recursive(remaining):
            # Add current element to front of each permutation
            permutations.append([current] + p)
            
    return permutations

# Alternative approach using itertools (more efficient)
from itertools import permutations

def get_permutations_itertools(lst):
    return list(permutations(lst))

# Example usage:
if __name__ == "__main__":
    test_list = [1, 2, 3]
    
    # Using recursive method
    print("Recursive method:")
    print(get_permutations_recursive(test_list))
    
    # Using itertools method
    print("\nItertools method:")
    print(get_permutations_itertools(test_list))
