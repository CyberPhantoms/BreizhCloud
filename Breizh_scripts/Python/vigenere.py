def caesar_encrypt(c: str, key: str) -> str:
    return chr(((ord(c)+ord(key)-2*ord("A"))%26) + ord("A"))

def caesar_decrypt(c: str, key:str) -> str:
    return chr(((ord(c)-ord(key)-2*ord("A")+26)%26) + ord("A"))

def vigenere_encrypt(text: str, key: str) -> str:
    res = []
    for (i, c) in enumerate(text):
        res.append(caesar_encrypt(c, key[i%len(key)]))
    return "".join(res)
    
def vigenere_decrypt(text: str, key: str) -> str:
    res = []
    for (i, c) in enumerate(text):
        res.append(caesar_decrypt(c, key[i%len(key)]))
    return "".join(res)

