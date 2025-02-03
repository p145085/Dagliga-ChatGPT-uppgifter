#20. **Skapa en filindexerare som använder hashning för att identifiera dubbletter i en katalog.**
import os
import hashlib
from collections import defaultdict

def hash_file(file_path):
    """Beräknar och returnerar hashvärdet för en fil."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            # Läs filen i bitar och uppdatera hashvärdet
            while chunk := f.read(8192):  # Läs 8 KB åt gången
                hash_sha256.update(chunk)
    except Exception as e:
        print(f"Fel vid bearbetning av filen {file_path}: {e}")
        return None
    return hash_sha256.hexdigest()

def find_duplicates(directory):
    """Letar efter dubbletter i en katalog baserat på hashvärden."""
    hashes = defaultdict(list)  # Nyckel: hash, Värde: lista av filvägar med samma hash
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash:
                if file_hash in hashes:
                    duplicates.append((file_path, hashes[file_hash][0]))  # Lägger till dubbletter
                hashes[file_hash].append(file_path)

    return duplicates

def print_duplicates(duplicates):
    """Skriver ut en lista med dubbletter."""
    if duplicates:
        print("Hittade följande dubbletter:")
        for dup1, dup2 in duplicates:
            print(f"Duplicerade filer:\n{dup1}\n{dup2}\n")
    else:
        print("Inga dubbletter hittades.")

if __name__ == "__main__":
    directory = input("Ange sökvägen till katalogen: ")
    duplicates = find_duplicates(directory)
    print_duplicates(duplicates)
