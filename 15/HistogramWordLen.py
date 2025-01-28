#15. **Implementera ett program som beräknar histogrammet för ordlängder i en textfil.**
import sys
from collections import Counter

def calculate_word_length_histogram(filename):
    try:
        # Läs in filen
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Dela upp texten i ord och beräkna längder
        words = text.split()
        word_lengths = [len(word.strip(",.!?;:\"'()[]{}")) for word in words]
        
        # Räkna förekomster av varje ordlängd
        histogram = Counter(word_lengths)
        
        # Sortera histogrammet efter ordlängd
        sorted_histogram = dict(sorted(histogram.items()))
        
        return sorted_histogram
    
    except FileNotFoundError:
        print(f"Filen {filename} kunde inte hittas.")
        sys.exit(1)
    except Exception as e:
        print(f"Ett fel uppstod: {e}")
        sys.exit(1)

def print_histogram(histogram):
    print("\nHistogram över ordlängder:")
    for length, count in histogram.items():
        print(f"Längd {length}: {'#' * count} ({count} ord)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Användning: python ordlangd_histogram.py <filnamn>")
        sys.exit(1)

    filename = sys.argv[1]
    histogram = calculate_word_length_histogram(filename)
    print_histogram(histogram)
