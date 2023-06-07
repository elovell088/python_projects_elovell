#IT 463 - Eric Lovell - Encryption Demo

from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()

private_key_file_name = input("Enter the file name for the private key: ")
file_out = open(private_key_file_name, "wb")
file_out.write(private_key)


public_key = key.publickey().export_key()

public_key_file_name = input("Enter the file name for the public key: ")
file_out = open("public_key.pem", "wb")
file_out.write(public_key)