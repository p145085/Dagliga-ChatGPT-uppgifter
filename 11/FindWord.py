#11. **Hitta ett ord i en fil:** Skapa ett program som söker efter ett specifikt ord i en textfil.

def search_word_in_file(file_path, word):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            found = False
            for line_num, line in enumerate(lines, start=1):
                if word.lower() in line.lower():  # Ignorera stora och små bokstäver
                    print(f"Ordet '{word}' hittades på rad {line_num}: {line.strip()}")
                    found = True
            if not found:
                print(f"Ordet '{word}' hittades inte i filen.")
    except FileNotFoundError:
        print(f"Filen {file_path} kunde inte hittas.")

# Exempel på användning
file_path = 'din_textfil.txt'  # Ange sökvägen till din textfil
word = 'sökord'  # Ange ordet du söker efter
search_word_in_file(file_path, word)
