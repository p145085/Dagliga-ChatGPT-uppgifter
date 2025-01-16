#8. **Implementera en funktion som kontrollerar om en matris är symmetrisk.**

def är_symmetrisk(matris):
    """
    Kontrollerar om en given matris är symmetrisk.
    
    En matris är symmetrisk om den är kvadratisk (antal rader = antal kolumner)
    och varje element uppfyller matris[i][j] == matris[j][i].
    
    :param matris: List[List[int]] - Tvådimensionell lista som representerar matrisen.
    :return: bool - True om matrisen är symmetrisk, annars False.
    """
    # Kontrollera om matrisen är kvadratisk
    n = len(matris)
    for rad in matris:
        if len(rad) != n:
            return False
    
    # Kontrollera symmetri
    for i in range(n):
        for j in range(i, n):  # Börja från i för att undvika dubbelkontroll
            if matris[i][j] != matris[j][i]:
                return False
    
    return True

# Exempel på användning
matris1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matris2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(är_symmetrisk(matris1))  # Output: True
print(är_symmetrisk(matris2))  # Output: False
