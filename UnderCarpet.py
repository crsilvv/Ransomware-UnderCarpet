from Crypto.Random import get_random_bytes # generate random key
from Crypto.Protocol.KDF import PBKDF2 # brute-force protection
from Crypto.Cipher import AES #  cryption
from Crypto.Util.Padding import pad, unpad #

# gerenation key
# generate_key = get_random_bytes(32)
# print (key)

salt = b'\x08\xa8\x95r\xa8W-\xacY\xf2\xab\xb8\x8d{Di\xa0\xb67>\xb7-lf,Y\xd1\xcd\xc3D\xfdY'
password = "Nala00110111#"

key = PBKDF2(password, salt, dkLen=32)

message = b"i dont know"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

print (ciphered_data)