from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_parameters
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDFExpand
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# storing the given parameter in Parameter.
parameters = b'-----BEGIN DH PARAMETERS-----\nMEYCQQDP+dSNnBRy4jbHTvr0YcEk0bMzisMy+p/k9VYCb+gPNU/OSDkmEX62YKTc\nj1QrAo8+f3du/bjdfVKfv71LWtxjAgEC\n-----END DH PARAMETERS-----\n'
#converting the parameter to object using the serialization  library.
pra_me = serialization.load_pem_parameters(parameters)
# Generate a private key for use in the exchange.
server_private_key = pra_me.generate_private_key()
# storing the given public key in pubk.
pubk= b'-----BEGIN PUBLIC KEY-----\nMIGaMFMGCSqGSIb3DQEDATBGAkEAz/nUjZwUcuI2x0769GHBJNGzM4rDMvqf5PVW\nAm/oDzVPzkg5JhF+tmCk3I9UKwKPPn93bv243X1Sn7+9S1rcYwIBAgNDAAJAYyRw\n2K7KvbqudRx9DQtKH/tAQjDtDMIw7hFWYslMFnE/t44wArXQ/wuo0NPhFL4b63R8\nJZA7cF7tP+CAj3WHFA==\n-----END PUBLIC KEY-----\n'
# converting the given public key to object using serialization function.
pbk = serialization.load_pem_public_key(pubk)
# genrating a peer_private key for use in exchange using the given parameter
peer_private_key = pra_me.generate_private_key()
# Genrating a shared key for the use in exchange with the help of the given public key.
shared_key = server_private_key.exchange(pbk)
# Perform key derivation using HKDF function.
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
   salt=None,
    info=b'handshake data',
 ).derive(shared_key)
# here we do the demeonstration in the reverse process to perform to check the final value.
sameshared_key = peer_private_key.exchange(
   server_private_key.public_key()
 )
samederived_key = HKDF(
   algorithm=hashes.SHA256(),
    length=32,
   salt=None,
    info=b'handshake data',
).derive(sameshared_key)
# in b checkin that the both the values of the derived key and same derived key.
B=derived_key == samederived_key
#printing the value of B
print(B)
#printing the derived key.
print(derived_key)
#Printing the shared_key which is actually the public key.
print(shared_key)




