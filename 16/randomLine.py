#16. **Slumpmässigt välja en rad från en fil:** Skriv ett program som väljer en slumpmässig rad från en textfil.

import random

def slumpmaessig_rad(filnamn):
    try:
        with open(filnamn, 'r', encoding='utf-8') as fil:
            rader = fil.readlines()
        if not rader:
            print("Filen är tom.")
            return None
        return random.choice(rader).strip()
    except FileNotFoundError:
        print(f"Filen '{filnamn}' kunde inte hittas.")
    except Exception as e:
        print(f"Ett fel inträffade: {e}")

# Användning
filnamn = "din_fil.txt"  # Byt ut detta mot din fil
vald_rad = slumpmaessig_rad(filnamn)
if vald_rad:
    print(f"Slumpmässig rad: {vald_rad}")
