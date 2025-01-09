#3. **Skapa en funktion som hittar den k:te största och minsta elementet i en lista.**

def find_kth_elements(lst, k):
    """
    Hittar det k:te största och minsta elementet i en lista.
    
    Args:
        lst (list): Listan med element.
        k (int): Positionen för det element som ska hittas.
    
    Returns:
        tuple: (k:te minsta elementet, k:te största elementet).
    """
    if not lst or k <= 0 or k > len(lst):
        raise ValueError("Ogiltig lista eller värde för k")
    
    # Sortera listan
    sorted_list = sorted(lst)
    
    # Hitta det k:te minsta och största elementet
    kth_smallest = sorted_list[k - 1]
    kth_largest = sorted_list[-k]
    
    return kth_smallest, kth_largest

# Exempelanvändning
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 3

kth_min, kth_max = find_kth_elements(lst, k)
print(f"Det {k}:te minsta elementet är {kth_min}")
print(f"Det {k}:te största elementet är {kth_max}")
