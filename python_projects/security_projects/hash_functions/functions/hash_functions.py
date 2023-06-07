#IT 463 - Eric Lovell - Hash Functions Assignment

from Crypto.Hash import SHA3_512
#from Crypto.Hash import SHA512

def createHash(password):
    """Function that creates a SHA3 512 Hash"""

    #Create Hash Object
    hash_object = SHA3_512.new()
    hash_object.update((password).encode("utf-8"))
    
    #First round of hash
    tmp_hash = hash_object.hexdigest()

    #Pull hash values for salt
    end_slice = len(tmp_hash)
    start_slice = end_slice - 10

    tmp_slice = tmp_hash[start_slice:end_slice]

    #Create new hash object for salted hash
    new_hash_object = SHA3_512.new()
    new_hash_object.update((tmp_hash + tmp_slice).encode("utf-8"))

    #Final hash with salt
    final_hash = new_hash_object.hexdigest()

    return final_hash
