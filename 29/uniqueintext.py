#29. Skapa ett program som räknar antalet unika ord i en text.

def count_unique_words(text):
    # Ta bort punktering och gör texten till gemener
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    # Dela upp texten i en lista av ord
    words = cleaned_text.split()
    # Använd en mängd för att få unika ord
    unique_words = set(words)
    # Returnera antalet unika ord
    return len(unique_words), unique_words

# Exempeltext
text = """
Detta är ett exempel. Ett enkelt exempel på en text för att demonstrera ett program!
"""

unique_count, unique_words = count_unique_words(text)
print(f"Antal unika ord: {unique_count}")
print("Unika ord:", unique_words)
