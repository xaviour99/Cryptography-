import os
import cryptography
import binascii
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

# creating a funcation to generate a salt for the given input password and we store the key.
def cret(salt, password):
#here salt is in bytes, length is in int and we provide the desired length of the key,n, r, p are all in int type as well.
#n is the memeory cost paramete,  r is block size parameter, p is parallization parameeter.
#kdf is the variable  where the Scrypt is generated and  stored.
    kdf = Scrypt(salt=salt, length=32, n=2 ** 14, r=8, p=1, )
#here key is a variable, where we generate the key  with the help of the given password and the created the scrypt.
    key = kdf.derive(password)
#here i'm returning the key to the function again.
    return key



# creating a verify fuction to verify the given passwor. And here we again generate a scryot and a key to verify witht he stored key.
def verify(salt, key, password):
# here salt is in bytes, length is in int and we provide the desired length of the key,n, r, p are all in int type as well.
# n is the memeory cost paramete,  r is block size parameter, p is parallization parameeter.
# kdf is the variable  where the Scrypt is generated and  stored.
    kdf = Scrypt(salt=salt, length=32, n=2 ** 14, r=8, p=1, )
#im using the binascii to convert the salt to hex
    binascii.a2b_hex(binascii.b2a_hex(salt))
# creating a try and except to verify the password and the generated key and the previosu key.
    try:
        kdf.verify(password, key)

# if the key matches it then  gives success else it throws the exception as the wrong password.
        return "success"
    except:
        return "wrong password"


if __name__ == "__main__":
# the os.urandom generates any random bytes for the salt.
    salt = os.urandom(16)
#Ps stores the input password and then we convet the password to bytes
    ps = input("pleas ent passd").encode()
#here we are create a variable key and then we call the create function and pass the salt and password and then store the key which is generated.
    key = cret(salt, ps)
#P again asks for the password to verify it with the key
    p = input("pleas ent passd")
#in print call the verify function and  pass the stored key and the entered password.
    print(verify(salt, key, p.encode()))