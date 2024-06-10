from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    with open(file_path + ".enc", 'wb') as f:
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)

# Gerar uma chave de 256 bits
key = get_random_bytes(32)
encrypt_file('example.txt', key)
