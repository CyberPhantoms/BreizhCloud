import cryptography
import sys
import os
import getpass

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

############################################################ Decipher with key (hardcoded) ############################################################
def dechiffre():
    ct = "C682093BF20041C1053FF19C9FE6AF71" # Texte chiffré

    s = "0123456789ABCDEF0123456789ABCDEF"  # Clé

    key = []

    # On transforme la clé en un tableau de bytes
    for i in range(len(s)//2):
        key.append(int(s[2*i:2*i+2], 16))
    
    # On transforme la clé en bytes object
    key = bytes(key)

    print(key)

    # On définit le chiffrement et le mode, ici ECB car un seul bloc à déchiffrer
    cipher = Cipher(algorithms.AES(key),modes.ECB())

    # On définit la méthode, ici on déchiffre
    decryptor = cipher.decryptor()

    # Bytes.fromhex(ct) pour avoir le même format que la clé, 
    print(decryptor.update(bytes.fromhex(ct)) + decryptor.finalize())

############################################################ Cipher function for a file ############################################################
def fileCipher():

    # On récup un vecteur d'initialisation
    iv = os.urandom(16)

    # Variables transparentes
    infile = sys.argv[2]
    outfile = sys.argv[3]

    # ??? je ne comprends pas ???
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=bytes([0]*16),
    iterations=480000,
    )

    # On lit direct le fichier en bytes et l'autre en ecriture
    f = open(infile, mode="rb").read()
    f2 = open(outfile, mode="wb")

    # Recup le mot de passe sans l'afficher dans le terminal
    mdp = str(getpass.getpass("Mot de passe de chiffrement : "))

    # Le padder (je ne sais plus à quoi il sert (histoire de taille entre clé et fichier normalement?))
    padder = padding.PKCS7(128).padder()
    clair_padde = padder.update(f) + padder.finalize()

    # Encodage de la clé afin de pouvoir l'utiliser
    key = kdf.derive(mdp.encode())
     
    # Définition du chiffrement, ici AES et son mode ici CBC
    cipher = Cipher(algorithms.AES(key),modes.CBC(iv))
    encryptor = cipher.encryptor()

    # On chiffre le fichier paddé
    ciphered_file = encryptor.update(clair_padde) + encryptor.finalize()

    # On écrit le vecteur au début du fichier afin de pouvoir le déchiffrer plus facilement et que ça soit plus clair
    f2.write(iv)
    # On écrit dans le fichier le chiffré
    f2.write(ciphered_file)

    f2.close()

############################################################ Decipher function for a file ############################################################
def fileDecipher():
    # Noms de variables assez transparents
    infile = sys.argv[2]
    outfile = sys.argv[3]

    # ??? je ne comprends toujours pas ???
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=bytes([0]*16),
    iterations=480000,
    )

    # On ouvre en lecture bytes le premier et écriture bytes le deuxième
    f = open(infile, mode="rb")
    f2 = open(outfile, mode="wb")

    # Récup du vecteur d'initialisation placé sur les 16 premiers octects (il ne faut pas que le fichier sois déja en lecture en mode bytes pour cette opération)
    iv = f.read(16)

    # On lit le fichier en bytes : c'est nécessaire
    f_bytes = f.read()

    # Recup le mot de passe sans l'afficher dans le terminal
    mdp = str(getpass.getpass("Mot de passe de déchiffrement : "))

    # Encodage de la clé pour son utilisation
    key = kdf.derive(mdp.encode())
    
    # Choix du chiffrement et son mode (idem fonction précédente)
    cipher = Cipher(algorithms.AES(key),modes.CBC(iv))

    decryptor = cipher.decryptor()
    deciphered_file = decryptor.update(f_bytes) + decryptor.finalize()

    # On écrit le clair dedans
    f2.write(deciphered_file)

    f2.close()

############################################################ RSA Encrypt ############################################################
def encryptRsa():
    clef = os.urandom(32)

    private_file = open("./RSA/key.pem", mode="rb")
    public_file = open("./RSA/key.pub.pem", mode="rb")

    private_key = serialization.load_pem_private_key(private_file.read(), password=None)
    public_key = serialization.load_pem_public_key(public_file.read())
    
    clechiffre = public_key.encrypt(
        clef,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    cledechiffre = private_key.decrypt(
        clechiffre,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(clef,"\n",cledechiffre)

############################################################ Main function ############################################################
if __name__ == '__main__': 

    # On trie les entrées
    if len(sys.argv) < 2:
        print("Too few arguments ! Use -h for usage.")
        exit(1)
    elif len(sys.argv) > 4:
        print("Error, too many arguments, use -h for usage.")
        print(sys.argv[0])
        exit(1)


    option = sys.argv[1]
    if option == "-e":
        fileCipher()  
    elif option == "-d":
        fileDecipher()
    elif option == "-h":
        print("Usage of the programm : \n \
            -e for encryption [File to encrypt] [Output file]\n \
            -d for decryption [File to decrypt] [Output file]\n \
            -R for RSA asymetric encryption, harcoded keys\n \
            -h For this menu.")
        exit(0)
    elif option == "-R":
        encryptRsa()
        print("RSA encryption with harcoded keys. Expiremental tho.")
    else:
        print("Wrong arguments.")
        exit(1)
