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

#HILL
import numpy as np

def clave_Matriz(clave,s,claveMatriz):
    count = 0
    for i in range(s):
        for j in range(s):
            claveMatriz[i][j] = ord(clave[count])-65
            count += 1
    return(np.matrix(claveMatriz))

def hillCifrar(texto, clave):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texto=texto.replace(" ","")
    texto=texto.upper()
    clave = clave.replace(" ","")
    clave= clave.upper()
    s=int(len(clave)**0.5)
    matrizClave = [[0] * s for i in range(s)]
    clave=clave_Matriz(clave,s,matrizClave)
    letrasIndice = dict(zip(letras, range(len(letras))))
    indiceLetras = dict(zip(range(len(letras)), letras))
    textoCifrado = ""
    textoIndices = []
    for i in texto:
        textoIndices.append(letrasIndice[i])
    split_P = [textoIndices[i : i + int(clave.shape[0])] for i in range(0, len(textoIndices), int(clave.shape[0]))]
    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]
        while P.shape[0] != clave.shape[0]:
            P = np.append(P, letrasIndice[" "])[:, np.newaxis]
        P=P.T
        numbers = np.dot(P, clave) % len(letras)
        numbers=numbers.T
        n = numbers.shape[0]  
        for i in range(n):
            number = int(numbers[i, 0])
            textoCifrado += indiceLetras[number]
    return textoCifrado

def inversaMatriz(matriz, mod):
    det = int(np.round(np.linalg.det(matriz)))
    det_inv = egcd(det, mod)[1] % mod
    invMatriz = (det_inv * np.round(det * np.linalg.inv(matriz)).astype(int) % mod)
    return invMatriz

def hillDescifrar(texto, clave):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texto=texto.replace(" ","")
    texto=texto.upper()
    clave = clave.replace(" ","")
    clave= clave.upper()
    s=int(len(clave)**0.5)
    matrizClave = [[0] * s for i in range(s)]
    clave=clave_Matriz(clave,s,matrizClave)
    clave=inversaMatriz(clave, len(letras))
    letrasIndice = dict(zip(letras, range(len(letras))))
    indiceLetras = dict(zip(range(len(letras)), letras))
    textoDescifrado = ""
    textoIndices = []
    for i in texto:
        textoIndices.append(letrasIndice[i])
    split_C = [textoIndices[i : i + int(clave.shape[0])]for i in range(0, len(textoIndices), int(clave.shape[0]))]
    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        C=C.T
        numbers = np.dot(C,clave) % len(letras)
        numbers=numbers.T
        n = numbers.shape[0]
        for i in range(n):
            number = int(numbers[i, 0])
            textoDescifrado += indiceLetras[number]
    return textoDescifrado