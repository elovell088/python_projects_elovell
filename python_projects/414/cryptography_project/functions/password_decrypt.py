# IT 463 - Eric Lovell - Decrypt Function
import json
from Crypto.Cipher import AES
from base64 import b64decode
from base64 import b64encode
import json

#Create while loop that validates minimum 16 character limit
proper_format = False
while not proper_format:
    user_password = input("Please enter password: ")
    if len(user_password) <= 15:
        print("Sorry, 16 characters minimum. Try again: ")
    else:
        password_bytes = user_password.encode("utf-8")
        proper_format = True

with open("my_password.json", "r") as file_load:
    saved_values = json.load(file_load)

ciphertext_bytes = b64decode(saved_values["ciphertext_password"])
iv = b64decode(saved_values["password_iv"])
print(ciphertext_bytes)

cipher_decrypt = AES.new(ciphertext_bytes, AES.MODE_CFB, iv=iv)
decrypted_plaintext_bytes = cipher_decrypt.decrypt(ciphertext_bytes)
decrypted_text = decrypted_plaintext_bytes.decode('utf-8')
print(decrypted_text)

