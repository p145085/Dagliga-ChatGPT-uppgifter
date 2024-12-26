#20. **Konvertera text till tal:** Läs en fil med textrepresentationer av siffror (t.ex. "ett", "två") och konvertera dem till numeriska värden.

from word2number import w2n

# Funktion för att konvertera ord till siffror
def convert_text_to_number(text):
    try:
        # Försök konvertera texten till ett nummer
        return w2n.word_to_num(text)
    except ValueError:
        # Om ordet inte kan konverteras, returnera originaltexten
        return text

# Läs filen med textrepresentationer av siffror
input_file = 'textfil.txt'
output_file = 'resultat.txt'

with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Konvertera varje rad och skriv till resultatfil
with open(output_file, 'w', encoding='utf-8') as file:
    for line in lines:
        words = line.strip().split()
        converted_words = [str(convert_text_to_number(word)) for word in words]
        file.write(' '.join(converted_words) + '\n')

print(f"Konverteringen är klar. Resultatet sparades i {output_file}.")
