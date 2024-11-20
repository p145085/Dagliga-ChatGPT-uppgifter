#16. Gör ett skript som renar en textfil från duplicerade rader.

def remove_duplicate_lines(input_file, output_file):
    try:
        # Läs in rader från filen
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # Ta bort duplicerade rader och behåll ordningen
        unique_lines = list(dict.fromkeys(lines))
        
        # Skriv de unika raderna till en ny fil
        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines(unique_lines)
        
        print(f"Duplicerade rader borttagna. Resultatet sparat i '{output_file}'")
    except FileNotFoundError:
        print(f"Filen '{input_file}' hittades inte.")
    except Exception as e:
        print(f"Ett fel uppstod: {e}")

# Ange filnamn
input_file = "input.txt"  # Filen som ska renas
output_file = "output.txt"  # Filen att spara resultatet i

# Kör funktionen
remove_duplicate_lines(input_file, output_file)
