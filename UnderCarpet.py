from Crypto.Random import get_random_bytes # generate random key
from Crypto.Protocol.KDF import PBKDF2 # brute-force protection
from Crypto.Cipher import AES #  cryption
from Crypto.Util.Padding import pad, unpad #

# gerenation key
key = get_random_bytes(32)

print (key)