#IT 463 - Eric Lovell - File Ecrypt functions

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


data = "This is my message".encode("utf-8")

file_out = open("encrypted_message.txt", "wb")

recipient_key = RSA.import_key(open("public_key.pem").read())
session_key = get_random_bytes(16)

#Use the public key to encrypt the AES session key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

#Use the AES session key to ecrypt the message
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

[file_out.write(item) for item in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]