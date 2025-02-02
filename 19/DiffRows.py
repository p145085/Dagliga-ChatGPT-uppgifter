#19. **Implementera ett program som jämför två filer och visar skillnaderna rad för rad.**
def jämför_filer(fil1, fil2):
    # Öppna och läs filerna
    with open(fil1, 'r') as f1, open(fil2, 'r') as f2:
        fil1_innehåll = f1.readlines()
        fil2_innehåll = f2.readlines()

    # Jämför filerna rad för rad
    rad_nummer = 1
    för rad1, rad2 i zip(fil1_innehåll, fil2_innehåll):
        om rad1 != rad2:
            print(f"Skillnad på rad {rad_nummer}:")
            print(f"Fil 1: {rad1.strip()}")
            print(f"Fil 2: {rad2.strip()}")
        rad_nummer += 1

    # Om filerna har olika antal rader
    om len(fil1_innehåll) > len(fil2_innehåll):
        print(f"Fil 1 har extra rader från rad {rad_nummer}:")
        för rad i fil1_innehåll[rad_nummer-1:]:
            print(f"Fil 1: {rad.strip()}")
    elif len(fil2_innehåll) > len(fil1_innehåll):
        print(f"Fil 2 har extra rader från rad {rad_nummer}:")
        för rad i fil2_innehåll[rad_nummer-1:]:
            print(f"Fil 2: {rad.strip()}")

# Användningsexempel
fil1 = "fil1.txt"
fil2 = "fil2.txt"
jämför_filer(fil1, fil2)
