#28. **Beräkna en diagonal summa:** Skriv ett program som beräknar summan av elementen i diagonalen av en kvadratisk matris.
def diagonal_sum(matrix):
    """
    Beräknar summan av elementen i huvuddiagonalen av en kvadratisk matris.
    
    :param matrix: 2D-lista (kvadratisk matris)
    :return: Summan av diagonalelementen
    """
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("Matriser måste vara kvadratiska!")
    
    return sum(matrix[i][i] for i in range(len(matrix)))

# Exempelanvändning
if __name__ == "__main__":
    # Exempel på en kvadratisk matris
    matris = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    try:
        summa = diagonal_sum(matris)
        print(f"Summan av diagonalelementen är: {summa}")
    except ValueError as e:
        print(e)
