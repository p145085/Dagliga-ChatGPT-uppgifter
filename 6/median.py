#6. **Beräkna medelvärdet:** Implementera en funktion som beräknar medelvärdet av en lista med tal.

def berakna_medelvarde(tal_lista):
    if len(tal_lista) == 0:
        return 0  # Returnerar 0 om listan är tom
    return sum(tal_lista) / len(tal_lista)

# Exempel på användning:
tal_lista = [1, 2, 3, 4, 5]
medelvarde = berakna_medelvarde(tal_lista)
print("Medelvärdet är:", medelvarde)
