import  cryptography
import os
import pickle

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# clef = os.urandom(32)
file_key = open("clefPourDoian.txt", "rb")

clef = file_key.read()

private_file = open("key.pem", mode="rb")
public_file = open("key.pub.pem", mode="rb")

private_key = serialization.load_pem_private_key(private_file.read(), password=None)
public_key = serialization.load_pem_public_key(public_file.read())

# clechiffre = public_key.encrypt(
#     clef,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )

cledechiffre = private_key.decrypt(
    clef,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(clef,"\n",cledechiffre)