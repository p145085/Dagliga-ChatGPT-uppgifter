#19. **Sortera en lista av tal från en fil:** Skriv ett program som läser en lista av tal från en fil och sorterar dem.

def sortera_tal(filnamn):
    try:
        with open(filnamn, 'r', encoding='utf-8') as fil:
            # Läs in alla rader, och konvertera till en lista av tal
            tal = [float(rad.strip()) for rad in fil if rad.strip()]
        # Sortera talen
        tal.sort()
        return tal
    except FileNotFoundError:
        print(f"Filen '{filnamn}' kunde inte hittas.")
        return []
    except ValueError:
        print("Filen innehåller ogiltiga värden som inte kan konverteras till tal.")
        return []
    except Exception as e:
        print(f"Ett fel inträffade: {e}")
        return []

# Användning
filnamn = "tal.txt"  # Byt ut detta mot din fil
sorterade_tal = sortera_tal(filnamn)
if sorterade_tal:
    print("Sorterade tal:")
    print(sorterade_tal)
