#IT 463 - Eric Lovell - Encrypt Functions
from Crypto.Cipher import AES
from base64 import b64encode
import json

#Start while loop until string over 15 characters long is entered
proper_format = False
while not proper_format:
    key = input("Please enter password: ")
    if len(key) <= 15:
        print("Sorry, 16 characters minimum. Try again: ")
    else:
        #Encode into byte format
        key_bytes = key.encode('utf-8')
        proper_format = True

#Create AES configurations and mode
cipher_encrypt = AES.new(key_bytes, AES.MODE_CFB)

#Get initialization vector information
iv_bytes = cipher_encrypt.iv
iv = b64encode(iv_bytes).decode('utf-8')

#Encrypt data
cipher_text_bytes = cipher_encrypt.encrypt(key_bytes)
ciphertext = b64encode(cipher_text_bytes).decode('utf-8')

#Print cipher texts
print("\nCipher Text: " + ciphertext)
print("IV: " + iv + "\n")

#Save cipher values in text files
decrypt_values_save = {"ciphertext_password" : ciphertext, "password_iv" : iv}
with open("my_password.json", "w") as file_store:
    json.dump(decrypt_values_save, file_store)

