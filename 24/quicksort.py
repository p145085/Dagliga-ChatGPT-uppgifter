#24. Implementera en sorteringsalgoritm (t.ex. quicksort).

def quicksort(lista):
    # Om listan är tom eller har ett element är den redan sorterad
    if len(lista) <= 1:
        return lista
    
    # Välj ett pivot-element (vi tar det sista elementet här)
    pivot = lista[-1]
    
    # Dela upp listan i tre delar: mindre än pivot, lika med pivot och större än pivot
    mindre = [x for x in lista[:-1] if x <= pivot]
    större = [x for x in lista[:-1] if x > pivot]
    
    # Anropa quicksort rekursivt och kombinera resultaten
    return quicksort(mindre) + [pivot] + quicksort(större)

# Testa algoritmen
if __name__ == "__main__":
    lista = [8, 3, 1, 7, 0, 10, 2]
    print("Osorterad lista:", lista)
    sorterad_lista = quicksort(lista)
    print("Sorterad lista:", sorterad_lista)
