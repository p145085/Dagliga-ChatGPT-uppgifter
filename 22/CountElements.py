#22. **Räkna förekomster av ett element i en lista:** Skriv en funktion som returnerar hur många gånger ett specifikt element förekommer i en lista.
def räkna_förekomster(lista, element):
    """
    Räknar antalet gånger ett element förekommer i en lista.

    :param lista: Listan som ska undersökas.
    :param element: Elementet vars förekomster ska räknas.
    :return: Antalet förekomster av elementet i listan.
    """
    return lista.count(element)

# Exempelanvändning
min_lista = [1, 2, 3, 2, 4, 2, 5]
element = 2
antal = räkna_förekomster(min_lista, element)
print(f"Elementet {element} förekommer {antal} gånger i listan.")
