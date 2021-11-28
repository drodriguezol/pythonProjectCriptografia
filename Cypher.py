#Funciones de criptación y desencriptación

#DESPLAZMIENTO CIPHER
def desplazamientoCifrar(text,s):
    text=text.upper()
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        result += chr(((ord(char) + s-65) % 26)+65)
    return result

def desplazamientoDescifrar(text,s):
    text.upper()
    result=""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) -(s-65)) % 26 +65 )
    return result