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
    texto.upper()
    resultado=""
    for i in range(len(texto)):
        char = texto[i]
        resultado += chr((ord(char) -(clave-65)) % 26 +65 )
    return resultado

#AFFINE
def affineCifrar(texto, clave):
    texto=texto.upper()
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
    return ''.join([ chr((( gcd(clave[0], 26)*(ord(c) - ord('A') - clave[1]))
                    % 26) + ord('A')) for c in texto])