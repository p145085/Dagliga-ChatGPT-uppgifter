#26. Bygg en hash-tabell med kollisionshantering.
class HashTable:
    def __init__(self, size=10):
        """Skapa en hash-tabell med angiven storlek."""
        self.size = size
        self.table = [[] for _ in range(self.size)]  # En lista med tomma listor (separate chaining)

    def _hash(self, key):
        """Beräkna hash-värdet för en given nyckel."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Lägg till eller uppdatera ett nyckel-värde-par i hash-tabellen."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Uppdatera värdet om nyckeln redan finns
                return
        self.table[index].append([key, value])  # Lägg till ny nyckel-värde-par

    def get(self, key):
        """Hämta värdet för en given nyckel."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Nyckeln hittades inte

    def remove(self, key):
        """Ta bort ett nyckel-värde-par från hash-tabellen."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        print(f"Nyckeln '{key}' hittades inte.")

    def display(self):
        """Visa hash-tabellen."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# Exempel på användning
hash_table = HashTable(size=5)

# Lägg till nyckel-värde-par
hash_table.insert("äpple", 10)
hash_table.insert("banan", 20)
hash_table.insert("körsbär", 30)

# Hantera kollision (exempel med samma hash)
hash_table.insert("äpple", 15)  # Uppdatera värdet för "äpple"

# Hämta värden
print("Värde för 'äpple':", hash_table.get("äpple"))
print("Värde för 'banan':", hash_table.get("banan"))

# Ta bort en nyckel
hash_table.remove("banan")

# Visa hash-tabellen
hash_table.display()
