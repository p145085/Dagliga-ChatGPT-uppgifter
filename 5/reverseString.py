#**Omvänd sträng:** Skriv ett program som tar en sträng och returnerar dess omvända.

def omvandla_sträng():
    # Tar en sträng från användaren
    sträng = input("Skriv in en sträng: ")
    # Returnerar den omvända strängen
    omvänd_sträng = sträng[::-1]
    print(f"Den omvända strängen är: {omvänd_sträng}")

# Kör funktionen
omvandla_sträng()
