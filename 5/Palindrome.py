#5. Bygg ett program som kontrollerar om en sträng är en palindrom.
def is_palindrome(s):
    # Filtrera strängen och jämför med dess omvända
    filtered = ''.join(filter(str.isalnum, s)).lower()
    return filtered == filtered[::-1]

# Testa funktionen
print(is_palindrome("Able was I ere I saw Elba"))  # Output: True
print(is_palindrome("Python"))  # Output: False
