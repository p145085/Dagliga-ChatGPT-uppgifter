#11. **Bygg ett skript som analyserar en loggfil och extraherar mönster för felmeddelanden.**
import re

def extract_errors(log_file):
    # Definiera en lista av felmönster som du vill extrahera
    error_patterns = [
        r"ERROR.*",  # Felmeddelanden som börjar med "ERROR"
        r"Exception.*",  # Felmeddelanden som innehåller "Exception"
        r"Fail.*",  # Felmeddelanden som innehåller "Fail"
        r"Stack trace.*"  # Felmeddelanden som innehåller "Stack trace"
    ]
    
    # Kombinera mönstren till ett enda regex-mönster
    combined_pattern = '|'.join(error_patterns)

    # Öppna loggfilen och extrahera felmeddelanden
    with open(log_file, 'r') as file:
        log_data = file.read()

    errors = re.findall(combined_pattern, log_data)

    return errors

# Användningsexempel
log_file_path = 'loggfil.log'  # Byt ut med din filväg
errors = extract_errors(log_file_path)

if errors:
    print("Felmeddelanden funna:")
    for error in errors:
        print(error)
else:
    print("Inga felmeddelanden hittades.")
