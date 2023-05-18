#IT 463 - Eric Lovell Symmetric Encryption Programming Lab Exercise
from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode
import json

message = "The stored values match"
message_bytes = message.encode('utf-8')

pass_validated = False
while not pass_validated:
    plain_text_pass = input("Enter password: ")
    if len(plain_text_pass) != 16:
        print("You entered an invalid character amount. Please try again: ")
    else:
        pass_validated = True

plain_text_bytes = plain_text_pass.encode('utf-8')

cipher_encrypt = AES.new(plain_text_bytes, AES.MODE_CFB)
iv_bytes = cipher_encrypt.iv

iv = b64encode(iv_bytes).decode('utf-8')

#Byte representation of cipher text - b'messycharacters
cipher_text_bytes = cipher_encrypt.encrypt(plain_text_bytes)

#Base64 version - Nice and clean ciphertext
cipher_text = b64encode(cipher_text_bytes).decode('utf-8')

ciphertext_values = {"ciphertext_password" : cipher_text, "password_iv" : iv}

with open("my_password.json", "w") as file_store:
    json.dump(ciphertext_values, file_store)
 
print(plain_text_pass)
print(iv_bytes)
print(iv)
print(cipher_text_bytes)
print(cipher_text)