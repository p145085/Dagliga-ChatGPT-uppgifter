#21. **Hitta ett element i en osorterad lista:** Implementera en linjär sökning.

def linjar_sokning(lista, element):
    """
    Utför en linjär sökning i en osorterad lista.
    
    Args:
        lista (list): Listan där vi letar efter elementet.
        element (any): Elementet vi letar efter.
        
    Returns:
        int: Index för elementet om det hittas, annars -1.
    """
    for i in range(len(lista)):
        if lista[i] == element:
            return i  # Returnera index för det första funna elementet.
    return -1  # Om elementet inte finns i listan.

# Exempelanvändning:
lista = [3, 5, 2, 9, 1]
element = 9

resultat = linjar_sokning(lista, element)

if resultat != -1:
    print(f"Elementet {element} hittades på index {resultat}.")
else:
    print(f"Elementet {element} hittades inte i listan.")
