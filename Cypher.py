#Funciones de criptación y desencriptación

#DESPLAZAMIENTO
def desplazamientoCifrar(texto,clave):
    texto=texto.upper()
    resultado = ""

    for i in range(len(texto)):
        char = texto[i]
        resultado += chr(((ord(char) + clave-65) % 26)+65)
    return resultado

def desplazamientoDescifrar(texto,clave):
    texto=texto.upper()
    resultado=""
    for i in range(len(texto)):
        char = texto[i]
        resultado += chr((ord(char) -(clave-65)) % 26 +65 )
    return resultado


#AFFINE
def affineCifrar(texto, clave):
    texto=texto.upper()
    if  gcd(clave[0],26)==0:
      return 0
    else:
      return ''.join([ chr((( clave[0]*(ord(t) - ord('A')) + clave[1] ) % 26)
                  + ord('A')) for t in texto.upper() ])
                  
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def gcd(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return 0
    else:
        return x % m

def affineDescifrar(texto, clave):
    texto=texto.upper()
    if  gcd(clave[0],26)==0:
      return 0
    else:
      return ''.join([ chr((( gcd(clave[0], 26)*(ord(c) - ord('A') - clave[1]))
                    % 26) + ord('A')) for c in texto])

#VIGENERE
def generarClave(texto, clave):
    clave = list(clave)
    if len(texto) == len(clave):
        return(clave)
    else:
        for i in range(len(texto)-len(clave)):
            clave.append(clave[i % len(clave)])
    return("".join(clave))
     
def vigenereCifrar(texto, clave):
    texto=texto.upper()
    clave=clave.replace(" ","")
    clave=clave.upper()
    clave = generarClave(texto,clave)
    textoCifrado = []
    for i in range(len(texto)):
        x = (ord(texto[i]) +
             ord(clave[i])) % 26
        x += ord('A')
        textoCifrado.append(chr(x))
    return("" . join(textoCifrado))
     
def vigenereDescifrar(texto, clave):
    texto=texto.upper()
    clave=clave.replace(" ","")
    clave=clave.upper()
    clave = generarClave(texto,clave)
    textoDescifrado = []
    for i in range(len(texto)):
        x = (ord(texto[i]) -
             ord(clave[i]) + 26) % 26
        x += ord('A')
        textoDescifrado.append(chr(x))
    return("" . join(textoDescifrado))

#SUSTITUCIÓN

#Random para generar la clave en caso de que el usuario no lo coloque
def sustitucionCifrar(texto, clave, letras):
    texto=texto.replace(" ","")
    texto=texto.upper()
    duplas = dict(zip(letras, clave))
    return ''.join(duplas.get(i) for i in texto)

def sustitucionDescifrar(texto, clave):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto=texto.replace(" ","")
    texto=texto.upper()
    duplas = dict(zip(clave, letras))
    return ''.join(duplas.get(i) for i in texto)