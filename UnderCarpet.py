import os
from Crypto.Random import get_random_bytes # generate random key
from Crypto.Protocol.KDF import PBKDF2 # brute-force protection
from Crypto.Cipher import AES #  cryption
from Crypto.Util.Padding import pad, unpad #



# gerenation key
# key = get_random_bytes(32)
# print (key) ↓
key = b'\tL\xc2\xfdI\x08\xe6\xd4\xedd\xdcWe\xcfJ\xf1\xae\x15J\x81\xe6\x1fq\xab?\xf8\xf8\xd0\xa7\x8e"s'
# Specify the directory to encrypt/decrypt
directory = 'Nova pasta'



# Encrypt
def pad(data):
    padding_length = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding_length]) * padding_length


def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(file_path, 'rb') as f:
        plaintext = f.read()
    
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)

    with open(file_path, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)


def encrypt_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)



# Decrypt
def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        iv = f.read(AES.block_size)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    unpadded_data = unpad(decrypted_data)

    with open(file_path, 'wb') as f:
        f.write(unpadded_data)


def decrypt_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)



# Encrypt all files in the directory
encrypt_directory(directory, key)

# Decrypt all files in the directory
decrypt_directory(directory, key)