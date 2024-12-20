#14. **Sammanfoga två textfiler:** Gör ett program som kombinerar innehållet från två textfiler till en.

def merge_files(file1, file2, output_file):
    try:
        # Öppna de två ingående filerna och läs deras innehåll
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            content1 = f1.read()
            content2 = f2.read()
        
        # Skriv innehållet till utfilen
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(content1)
            out.write("\n")  # Lägg till en ny rad mellan filerna (valfritt)
            out.write(content2)
        
        print(f"Filerna '{file1}' och '{file2}' har sammanfogats till '{output_file}'.")
    except FileNotFoundError as e:
        print(f"Fel: {e}")
    except Exception as e:
        print(f"Ett oväntat fel inträffade: {e}")

# Ange filnamnen
file1 = input("Ange den första filen: ")
file2 = input("Ange den andra filen: ")
output_file = input("Ange namnet på utfilen: ")

merge_files(file1, file2, output_file)
