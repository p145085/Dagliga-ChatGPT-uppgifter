#7. **Hitta dubbletter i en lista:** Skriv ett program som identifierar alla dubbletter i en lista.

def hitta_dubbletter(lst):
    dubbletter = []
    sett = set()
    for item in lst:
        if item in sett:
            dubbletter.append(item)
        else:
            sett.add(item)
    return dubbletter

# Exempelanvändning:
lista = [1, 2, 3, 4, 2, 5, 6, 3, 7]
dubbletter = hitta_dubbletter(lista)
print("Dubbletter:", dubbletter)
