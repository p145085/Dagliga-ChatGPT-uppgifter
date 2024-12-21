#15. **Lista alla filer i en katalog:** Bygg ett program som listar alla filer i en given katalog.

import os

def list_files_in_directory(directory):
    try:
        # Hämtar alla filer i den angivna katalogen
        files = os.listdir(directory)
        
        # Filtrerar bort eventuella undermappar
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        
        if files:
            print("Filer i katalogen:")
            for file in files:
                print(file)
        else:
            print("Inga filer hittades i katalogen.")
    except FileNotFoundError:
        print(f"Katalogen '{directory}' hittades inte.")
    except PermissionError:
        print(f"Du har inte behörighet att komma åt katalogen '{directory}'.")

# Användaren matar in sökvägen till katalogen
directory = input("Ange sökvägen till katalogen: ")
list_files_in_directory(directory)
