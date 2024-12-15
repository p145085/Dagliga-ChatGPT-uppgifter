#9. **Multiplikationstabell:** Generera en multiplikationstabell för ett givet tal.

# Funktion för att generera en multiplikationstabell
def multiplikationstabell(tal, max_num=10):
    print(f"Multiplikationstabell för {tal}:")
    for i in range(1, max_num + 1):
        print(f"{tal} x {i} = {tal * i}")

# Ange vilket tal du vill ha tabellen för
givet_tal = int(input("Ange ett tal: "))
multiplikationstabell(givet_tal)
