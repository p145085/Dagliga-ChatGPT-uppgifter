#30. **Slumpmässig omordning av en lista:** Skriv ett program som blandar om en lista slumpmässigt.
import random

def slumpa_lista(lista):
    random.shuffle(lista)
    return lista

# Exempelanvändning
min_lista = [1, 2, 3, 4, 5]
slumpad_lista = slumpa_lista(min_lista)
print(slumpad_lista)
