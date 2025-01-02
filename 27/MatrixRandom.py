#27. **Fyll en matris:** Skapa en matris av specifik storlek och fyll den med slumpmässiga heltal.
import numpy as np

# Ange storleken på matrisen, t.ex. 3x3
rows = 3
cols = 3

# Skapa en matris med slumpmässiga heltal mellan 1 och 100
matrix = np.random.randint(1, 101, size=(rows, cols))

# Skriv ut matrisen
print(matrix)
