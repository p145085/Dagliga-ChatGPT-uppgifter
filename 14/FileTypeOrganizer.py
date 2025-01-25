#14. **Bygg ett system som automatiskt organiserar filer i en katalog baserat på filtyp.**
import os
import shutil

# Definiera en funktion för att skapa mappar baserat på filtyper
def sort_files_by_extension(directory):
    # Hämta alla filer i katalogen
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Kontrollera om det är en fil (inte en mapp)
        if os.path.isfile(file_path):
            # Få filens filändelse
            file_extension = filename.split('.')[-1]

            # Skapa en mapp baserat på filtypen om den inte finns
            folder_path = os.path.join(directory, file_extension)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Flytta filen till rätt mapp
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Flyttade {filename} till {folder_path}")

# Ange katalogen som ska sorteras
directory = "/sökväg/till/din/katalog"
sort_files_by_extension(directory)
