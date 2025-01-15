#7. **Lös Josephus-problemet med en iterativ metod.**

def josephus(n, k):
    # Start med position 0 (1-indexerad blir det 1)
    result = 0
    for i in range(2, n + 1):  # Iterera från 2 till n
        result = (result + k) % i  # Uppdatera positionen
    return result + 1  # Omvandla till 1-indexerat

# Exempelanvändning:
n = 7  # Antal personer
k = 3  # Var tredje person elimineras
winner = josephus(n, k)
print(f"Den överlevande personen står på position {winner}.")
