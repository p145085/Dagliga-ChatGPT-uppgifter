#12. **Radera tomma rader i en fil:** Bygg ett skript som tar bort alla tomma rader från en textfil.

# Radera tomma rader från en textfil
def remove_empty_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if line.strip():  # Kontrollera om raden inte är tom
                    outfile.write(line)
        print(f"Tomma rader har tagits bort och resultatet har sparats i '{output_file}'.")
    except FileNotFoundError:
        print(f"Filen '{input_file}' hittades inte.")
    except Exception as e:
        print(f"Ett fel uppstod: {e}")

# Exempelanvändning
input_file = 'filnamn.txt'  # Ange din indatafil
output_file = 'rensad_fil.txt'  # Ange din utdatafil
remove_empty_lines(input_file, output_file)
