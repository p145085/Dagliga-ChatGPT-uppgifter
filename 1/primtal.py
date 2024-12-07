#1. **Kontrollera primtal:** Skriv ett program som avgör om ett tal är ett primtal.

def är_primtal(tal):
    if tal <= 1:
        return False  # Tal mindre än eller lika med 1 är inte primtal
    for i in range(2, int(tal**0.5) + 1):
        if tal % i == 0:
            return False  # Hittade en faktor, inte ett primtal
    return True  # Inga faktorer hittades, det är ett primtal

# Testa funktionen
nummer = int(input("Ange ett tal: "))
if är_primtal(nummer):
    print(f"{nummer} är ett primtal!")
else:
    print(f"{nummer} är inte ett primtal.")
