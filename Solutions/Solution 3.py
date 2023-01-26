#import XOR as XOR
from collections import Counter
import pyaes, pbkdf2, binascii, os, secrets
import secret as secret
from bitstring import BitArray
from pyaes import AES
import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter

#In plaintext1 im giving the message A and encoding it to bytes.
plaintext1 = ("I'll give you 500 and that's my last offer.").encode()
#In E we store the encrypted value which was given in the question.
E = b"\xef@\x92<$J\xb2\x8c\xbc\xabl'\x016\xd2{W-8\xcas\x83*\xa1\xef)\xc0\xda\x7fe\xab\xb1\x94\x7fJ\x98\xc8\xeei|'t\xb4"

#Creating a function to do byte xor where the ba1 is on byted message and ba2 is fo the passed key.
def byte_xor(ba1, ba2):
#returning the key value after the xor is done. here the value a is xor with b till the zip ba1 and ba2 is completed.
    return bytes([a ^ b for a, b in zip(ba1, ba2)])
#key stores the xor value and here we call the byte_xor function and pass E and plaintext1
key =  byte_xor(E , plaintext1)
#Plaintext2 the message2 is stored and is encodes to bytes.
plaintext2 = ("I'll give you 100 and that's my last offer.").encode()
# in Key1 we all the bytes_xor and pass the key and plaintext2 to do xor and store the generated value in key1.
key1 = byte_xor(key,plaintext2)
#here printing the key which is stored in the key1.
print("print key1",key1)


