#19. Implementera ett program som laddar ner filer från en URL.

import requests

def download_file(url, output_file):
    try:
        # Skicka en GET-begäran till URL:en
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Kontrollera om begäran lyckades
        
        # Spara innehållet till fil
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Filen har laddats ner och sparats som {output_file}")
    
    except requests.exceptions.RequestException as e:
        print(f"Ett fel uppstod: {e}")

# Exempel på användning
if __name__ == "__main__":
    file_url = input("Ange URL för filen som ska laddas ner: ")
    output_path = input("Ange filnamnet för att spara (inkl. sökväg): ")
    download_file(file_url, output_path)
