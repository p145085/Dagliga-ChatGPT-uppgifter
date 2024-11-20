#18. Kryptera och dekryptera text från en fil.

from cryptography.fernet import Fernet

# Generera en nyckel och spara den i en fil (kör detta bara en gång)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Ladda nyckeln från filen
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Kryptera text och spara till en fil
def encrypt_file(input_file, output_file):
    key = load_key()
    fernet = Fernet(key)
    
    with open(input_file, "r", encoding="utf-8") as file:
        data = file.read()
    
    encrypted_data = fernet.encrypt(data.encode())
    
    with open(output_file, "wb") as file:
        file.write(encrypted_data)

# Dekryptera text från en fil och spara som läsbar text
def decrypt_file(input_file, output_file):
    key = load_key()
    fernet = Fernet(key)
    
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(decrypted_data)

# Exempel på användning
encrypt_file("plaintext.txt", "encrypted.txt")
decrypt_file("encrypted.txt", "decrypted.txt")