def get_index(tableau):
    max_value = max(tableau)
    for i in range(len(tableau)):
        if tableau[i] == max_value:
            return i


def decipher_text():

    ciphered_text = "WRARCRAFRCNFDHVYLNVGQROBAARBHQRZNHINVFRFVGHNGVBA"
    decalage = 0
    frequences_ref = {'A': 0.0815, 'N': 0.0712, 'B': 0.0097, 'O': 0.0528, 'C': 0.0315, 'P': 0.028, 'D': 0.0373, 'Q': 0.0121, 'E': 0.1739, 'R': 0.0664, 'F': 0.0112, 'S': 0.0814, 'G': 0.0097, 'T': 0.0722, 'H': 0.0085, 'U': 0.0638, 'I': 0.0731, 'V': 0.0164, 'J': 0.0045, 'W': 0.0003, 'K': 0.0002, 'X': 0.0041, 'L': 0.057, 'Y': 0.0028, 'M': 0.0287, 'Z': 0.0015}
    tab = []
    reponse = []

    for i in range(26):
        decalage = i
        deciphered_text = ""
        occurences = {}

        for lettre in ciphered_text:  
                nombre = ord(lettre)
                nombre -= ord('A')
                nombre += decalage
                nombre = nombre % 26
                nombre += ord('A')
                lettre_finale = chr(nombre)
                deciphered_text += lettre_finale

        for char in deciphered_text:    
            if char in occurences:
                occurences[char] += 1   
            else:
                occurences[char] = 1

        reponse.append(deciphered_text)
        scalaire = sum([occurences[lettre]*frequences_ref[lettre] for lettre in occurences])
        tab.append(scalaire)
        max_value = max(tab)
        index = get_index(tab)
        
    print("valeur max :", max_value, "le décalage est de :", index )
    print("Texte déchiffré : ", reponse[index])



if __name__ == '__main__':
    decipher_text()