#IT 463 - Eric Lovell - Encyption Assignment Demo
from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode
import json

plaintext = "This is my message"
plaintext_bytes = plaintext.encode('utf-8')

key = "MyPass123addmore"
key_bytes = key.encode('utf-8')

cipher_encrypt = AES.new(key_bytes, AES.MODE_CFB)
iv_bytes = cipher_encrypt.iv

iv = b64encode(iv_bytes).decode('utf-8')

cipher_text_bytes = cipher_encrypt.encrypt(plaintext_bytes)
ciphertext = b64encode(cipher_text_bytes).decode('utf-8')

print(cipher_text_bytes)
print(ciphertext)
print(iv)

decrypt_values_save = {"ciphertext_saved" : ciphertext, "iv_saved" : iv}
with open("stored_values.json", "w") as file_store:
    json.dump(decrypt_values_save, file_store)

with open("stored_values.json", "r") as file_load:
    saved_values = json.load(file_load)

#ciphertext_decrypt = b64decode(ciphertext)
#iv_decrypt = b64decode(iv)
ciphertext_decrypt = b64decode(saved_values["ciphertext_saved"])
iv_decrypt = b64decode(saved_values["iv_saved"])


cipher_decrypt = AES.new(key_bytes, AES.MODE_CFB, iv=iv_decrypt)
decrypted_plaintext_bytes = cipher_decrypt.decrypt(ciphertext_decrypt)
decrypted_plaintext = decrypted_plaintext_bytes.decode()


print(decrypted_plaintext_bytes)
print(decrypted_plaintext) 