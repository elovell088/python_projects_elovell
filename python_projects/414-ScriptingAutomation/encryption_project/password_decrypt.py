from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode
import json


pass_validated = False
while not pass_validated:
    plain_text_pass = input("Enter password: ")
    if len(plain_text_pass) != 16:
        print("You entered an invalid character amount. Please try again: ")
    else:
        pass_validated = True

plain_text_bytes = plain_text_pass.encode('utf-8')

with open("my_password.json", 'r') as file_load:
    saved_values = json.load(file_load)

loaded_cipher = saved_values["ciphertext_password"]
loaded_iv = saved_values["password_iv"]

loaded_cipher_bytes = b64decode(loaded_cipher)
loaded_iv_bytes = b64decode(loaded_iv)


decrypt_cipher = AES.new(loaded_cipher_bytes, AES.MODE_CFB, iv=loaded_iv_bytes)
decrypted_plaintext_bytes = decrypt_cipher.decrypt(loaded_cipher_bytes)

decrypted_ciphertext = decrypted_plaintext_bytes.decode


print(loaded_cipher)
print(decrypted_plaintext_bytes)
print(decrypted_ciphertext)
print(loaded_iv)
print(loaded_cipher_bytes)
