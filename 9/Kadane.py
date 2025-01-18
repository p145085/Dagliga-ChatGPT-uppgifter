#9. **Skapa en algoritm som beräknar det största sammanhängande subarray-summan (Kadane’s algoritm).**
def max_subarray_sum(arr):
    """Beräknar den största sammanhängande subarray-summan."""
    max_sum = float('-inf')  # Initialisera med negativ oändlighet
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)  # Uppdatera den aktuella summan
        max_sum = max(max_sum, current_sum)  # Uppdatera den största summan

    return max_sum


# Exempelanvändning
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultat = max_subarray_sum(array)
print(f"Den största sammanhängande subarray-summan är: {resultat}")
