#24. **Slumpmässigt välj n element från en lista:** Skriv ett program som väljer n slumpmässiga element från en lista.
import random

def slumpmässigt_välj(lista, n):
    if n > len(lista):
        raise ValueError("n kan inte vara större än listans längd.")
    return random.sample(lista, n)

# Exempelanvändning
min_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
antal_element = 3

slumpmässiga_element = slumpmässigt_välj(min_lista, antal_element)
print(f"De {antal_element} slumpmässigt valda elementen är: {slumpmässiga_element}")
