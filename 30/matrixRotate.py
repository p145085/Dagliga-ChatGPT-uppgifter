#30. Implementera en funktion för att rotera en matris medurs.
def rotera_matris(matris):
    """
    Roterar en matris medurs.
    
    :param matris: 2D-lista som representerar matrisen.
    :return: Ny roterad matris.
    """
    if not matris or not matris[0]:
        raise ValueError("Matrisen får inte vara tom.")
    
    # Transponerar matrisen och vänder varje rad
    roterad = [list(r) for r in zip(*matris[::-1])]
    return roterad

# Exempelanvändning
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

roterad_matris = rotera_matris(matris)
print("Originalmatris:")
for rad in matris:
    print(rad)

print("\nRoterad matris:")
for rad in roterad_matris:
    print(rad)
