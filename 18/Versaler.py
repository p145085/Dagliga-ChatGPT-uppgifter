#18. **Konvertera text till versaler:** Skapa ett program som läser från en fil och skriver ut allt i versaler.

# Funktion för att läsa från en fil och skriva ut i versaler
def konvertera_till_versaler(filnamn):
    try:
        # Öppnar filen i läsläge
        with open(filnamn, 'r', encoding='utf-8') as fil:
            innehall = fil.read()
        
        # Skriver ut innehållet i versaler
        print(innehall.upper())
    except FileNotFoundError:
        print(f"Filen '{filnamn}' kunde inte hittas.")
    except Exception as e:
        print(f"Ett fel inträffade: {e}")

# Huvudfunktion
if __name__ == "__main__":
    filnamn = input("Ange filens namn: ")
    konvertera_till_versaler(filnamn)
