from Crypto.Random import get_random_bytes # generate random key
from Crypto.Protocol.KDF import PBKDF2 # brute-force protection
from Crypto.Cipher import AES #  cryption
from Crypto.Util.Padding import pad, unpad #



# gerenation key
# key = get_random_bytes(32)
# print (key)



key = b'\tL\xc2\xfdI\x08\xe6\xd4\xedd\xdcWe\xcfJ\xf1\xae\x15J\x81\xe6\x1fq\xab?\xf8\xf8\xd0\xa7\x8e"s'



# encrypt
def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    with open(file_path, 'wb') as f:
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)



# decrypt

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    
    with open(file_path[:-4], 'wb') as f:
        f.write(plaintext)

decrypt_file('example.txt', key)
encrypt_file('example.txt', key)