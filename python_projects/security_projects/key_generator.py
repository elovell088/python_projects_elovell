#This code is for educational and training purposes only - EL
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


#Key Generation
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

private_key_filename = "my_private_key.pem"
file_out = open(private_key_filename, "wb")
file_out.write(private_key)

public_key_filename = "my_public_key.pem"
file_out = open(public_key_filename, "wb")
file_out.write(public_key)
