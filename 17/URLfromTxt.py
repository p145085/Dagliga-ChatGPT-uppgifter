#17. **Skapa ett program som söker efter alla URL:er i en textfil och sparar dem i en separat fil.**
import re

def extract_urls(input_file, output_file):
    # Regex för att matcha URL:er
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()
    
    urls = url_pattern.findall(content)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(urls))
    
    print(f"Hittade {len(urls)} URL:er. Sparade dem i {output_file}.")

# Exempel på användning
extract_urls('input.txt', 'output_urls.txt')
