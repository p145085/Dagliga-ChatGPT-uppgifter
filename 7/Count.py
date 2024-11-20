#7. Räkna antalet ord i en given sträng.

def count_words(s):
    return len(s.split())

# Testa funktionen
text = "Hello world! This is a test."
print(count_words(text))  # Output: 6
