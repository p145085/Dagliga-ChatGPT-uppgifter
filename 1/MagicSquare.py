#1. **Skriv en funktion som genererar ett magiskt kvadrat (magic square).**
def generate_magic_square(n):
    if n < 3 or n % 2 == 0:
        raise ValueError("Detta fungerar endast för udda heltal n >= 3.")

    # Skapa en tom kvadrat med 0:or
    magic_square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2  # Börja från mitten av första raden

    for num in range(1, n * n + 1):
        magic_square[i][j] = num  # Placera nästa tal

        # Förflyttning enligt Siamese-metoden: gå uppåt och åt höger
        new_i, new_j = (i - 1) % n, (j + 1) % n

        # Om platsen redan är upptagen, gå neråt istället
        if magic_square[new_i][new_j] != 0:
            new_i, new_j = (i + 1) % n, j

        i, j = new_i, new_j

    return magic_square

# Funktion för att skriva ut den magiska kvadraten
def print_magic_square(square):
    for row in square:
        print("\t".join(map(str, row)))

# Exempelanvändning
if __name__ == "__main__":
    try:
        n = int(input("Ange storleken på den magiska kvadraten (udda heltal >= 3): "))
        magic_square = generate_magic_square(n)
        print("\nDen genererade magiska kvadraten:")
        print_magic_square(magic_square)
    except ValueError as e:
        print(e)
