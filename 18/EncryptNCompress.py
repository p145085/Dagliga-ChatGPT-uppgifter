#18. **Skriv ett skript som krypterar och komprimerar en textfil.**
import gzip
import os
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode

def derive_key(password: str, salt: bytes) -> bytes:
    """Härled en 256-bitars nyckel från lösenordet och saltet"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_and_compress(input_file: str, output_file: str, password: str):
    """Läser en fil, komprimerar och krypterar den med AES-256 GCM"""
    salt = os.urandom(16)  # 16-byte slumpmässigt salt
    key = derive_key(password, salt)
    iv = os.urandom(12)  # 12-byte initialiseringsvektor för GCM
    
    # Läs och komprimera filen
    with open(input_file, 'rb') as f:
        compressed_data = gzip.compress(f.read())

    # Kryptera med AES-GCM
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(compressed_data) + encryptor.finalize()
    
    # Spara krypterad data, IV, salt och auth tag
    output = {
        "salt": urlsafe_b64encode(salt).decode(),
        "iv": urlsafe_b64encode(iv).decode(),
        "tag": urlsafe_b64encode(encryptor.tag).decode(),
        "data": urlsafe_b64encode(encrypted_data).decode(),
    }
    
    with open(output_file, 'w') as f:
        json.dump(output, f)

    print(f"Fil '{input_file}' har krypterats och sparats som '{output_file}'.")

def decrypt_and_decompress(input_file: str, output_file: str, password: str):
    """Läser en krypterad fil, dekrypterar och dekomprimerar den"""
    with open(input_file, 'r') as f:
        encrypted_json = json.load(f)

    # Läs metadata
    salt = urlsafe_b64decode(encrypted_json["salt"])
    iv = urlsafe_b64decode(encrypted_json["iv"])
    tag = urlsafe_b64decode(encrypted_json["tag"])
    encrypted_data = urlsafe_b64decode(encrypted_json["data"])

    key = derive_key(password, salt)

    # Dekryptera
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    compressed_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Dekomprimera och skriv ut
    with open(output_file, 'wb') as f:
        f.write(gzip.decompress(compressed_data))

    print(f"Fil '{input_file}' har dekrypterats och sparats som '{output_file}'.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Kryptera och komprimera en fil")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="encrypt eller decrypt")
    parser.add_argument("input_file", help="Fil att kryptera/dekryptera")
    parser.add_argument("output_file", help="Output-fil")
    parser.add_argument("password", help="Lösenord för kryptering/dekryptering")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_and_compress(args.input_file, args.output_file, args.password)
    else:
        decrypt_and_decompress(args.input_file, args.output_file, args.password)

#Encrypt and compress
#python script.py encrypt input.txt encrypted.json "hemligt_losenord"

#Decrypt and decompress
#python script.py decrypt encrypted.json output.txt "hemligt_losenord"
