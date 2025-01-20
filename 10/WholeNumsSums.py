#10. **Implementera en lösning för att beräkna alla möjliga sätt att dela upp ett heltal i summor.**
def partition(number):
    def _partition(number, max_value):
        if number == 0:
            yield []
        for i in range(min(number, max_value), 0, -1):
            for result in _partition(number - i, i):
                yield [i] + result

    return list(_partition(number, number))

# Exempelanvändning
n = 5
resultat = partition(n)
print(f"Alla sätt att dela upp {n} i summor:")
for p in resultat:
    print(p)
