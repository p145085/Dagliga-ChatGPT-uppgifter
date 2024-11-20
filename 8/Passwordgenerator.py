#8. Skapa en slumpmässig lösenordsgenerator.

import random
import string

class PasswordGenerator:
    def __init__(self):
        self.length = 8
        self.uppercase_count = 2
        self.number_count = 2
        self.special_count = 2

    def set_length(self, length):
        self.length = max(length, 4)  # Minsta längd på 4 för att säkerställa variation

    def set_uppercase_count(self, count):
        self.uppercase_count = count

    def set_number_count(self, count):
        self.number_count = count

    def set_special_count(self, count):
        self.special_count = count

    def generate(self):
        if self.length < self.uppercase_count + self.number_count + self.special_count:
            raise ValueError("Total specificerat antal tecken överstiger lösenordets längd.")

        # Generera tecken
        uppercase_chars = random.choices(string.ascii_uppercase, k=self.uppercase_count)
        number_chars = random.choices(string.digits, k=self.number_count)
        special_chars = random.choices(string.punctuation, k=self.special_count)
        lowercase_chars = random.choices(string.ascii_lowercase, k=self.length - len(uppercase_chars + number_chars + special_chars))

        # Kombinera och blanda tecken
        password_list = uppercase_chars + number_chars + special_chars + lowercase_chars
        random.shuffle(password_list)

        # Skapa lösenord som en sträng
        return ''.join(password_list)

# Användning
generator = PasswordGenerator()
generator.set_length(12)
generator.set_uppercase_count(3)
generator.set_number_count(4)
generator.set_special_count(2)

password = generator.generate()
print("Genererat lösenord:", password)
