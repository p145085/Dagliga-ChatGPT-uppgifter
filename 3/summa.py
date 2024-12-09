#**Beräkna summan av en lista:** Implementera en funktion som tar en lista av tal och returnerar summan.
def summa_av_lista(tal_lista):
    """
    Tar en lista av tal och returnerar summan.
    
    :param tal_lista: Listan av tal (t.ex. [1, 2, 3])
    :return: Summan av talen i listan
    """
    return sum(tal_lista)

# Exempelanvändning
min_lista = [1, 2, 3, 4, 5]
print(f"Summan av listan är: {summa_av_lista(min_lista)}")
