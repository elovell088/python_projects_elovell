from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import os

private_key = RSA.import_key(open("my_private_key.pem").read())

start_path = "\\myNewDirectory"  # Change this to your encrypted directory path
os.chdir(start_path)

for dirpath, dirnames, filenames in os.walk(start_path):
    for filename in filenames:
        file_to_decrypt = os.path.join(dirpath, filename)

        with open(file_to_decrypt, "rb") as file:
            encrypt_session_key, nonce, tag, ciphertext = [
                file.read(item) for item in (private_key.size_in_bytes(), 16, 16, -1)
            ]

        rsa_cipher = PKCS1_OAEP.new(private_key)
        session_key = rsa_cipher.decrypt(encrypt_session_key)

        aes_cipher = AES.new(session_key, AES.MODE_EAX, nonce)
        data = aes_cipher.decrypt_and_verify(ciphertext, tag)

        with open(file_to_decrypt, "wb") as file:
            file.write(data)
