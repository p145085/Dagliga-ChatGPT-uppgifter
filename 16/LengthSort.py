#16. **Läs en textfil och sortera meningar baserat på deras längd.**
# Funktion för att läsa filen och sortera meningarna efter längd
def sort_sentences_by_length(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Läs innehållet i filen
            text = file.read()
            
            # Dela upp texten i meningar (kan behöva justeras beroende på filens struktur)
            sentences = text.split('.')
            
            # Ta bort eventuella tomma strängar
            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
            
            # Sortera meningarna baserat på längd
            sorted_sentences = sorted(sentences, key=len)
            
            # Skriv ut sorterade meningar
            for sentence in sorted_sentences:
                print(sentence)
    
    except FileNotFoundError:
        print(f"Filen {file_path} hittades inte.")
    except Exception as e:
        print(f"Ett fel uppstod: {e}")

# Exempel på användning
file_path = 'din_fil.txt'  # Ange filens sökväg
sort_sentences_by_length(file_path)
