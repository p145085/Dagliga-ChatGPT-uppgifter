#13. **Räkna tecken i en fil:** Skriv ett program som läser en fil och räknar antalet tecken.
def räkna_tecken(filnamn):
    try:
        with open(filnamn, 'r', encoding='utf-8') as fil:
            innehåll = fil.read()
            antal_tecken = len(innehåll)
            print(f"Antalet tecken i filen '{filnamn}' är: {antal_tecken}")
    except FileNotFoundError:
        print(f"Filen '{filnamn}' hittades inte.")
    except Exception as e:
        print(f"Ett fel uppstod: {e}")

# Användning
filnamn = input("Ange filens namn: ")
räkna_tecken(filnamn)
