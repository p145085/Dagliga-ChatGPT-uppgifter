#26. **Hitta den längsta strängen i en lista:** Implementera en funktion som returnerar den längsta strängen i en lista.
def hitta_langsta_strang(listan):
    if not listan:
        return None  # Returnerar None om listan är tom
    return max(listan, key=len)

# Exempel
lista = ["äpple", "banan", "kiwi", "vattenmelon"]
resultat = hitta_langsta_strang(lista)
print(resultat)  # Output: vattenmelon
