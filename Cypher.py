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

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist') ######ventana emergenteee
    else:
        return x % m

def hillCifrar(texto, clave):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texto=texto.replace(" ","")
    texto=texto.upper()
    clave = clave.replace(" ","")
    clave= clave.upper()
    s=int(len(clave)**0.5)
    matrizClave = [[0] * s for i in range(s)]
    clave=clave_Matriz(clave,s,matrizClave)
    #para evitar aceptar matrices con determinante 0
    warning=inversaMatriz(clave, len(letras))
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
    det2= int(np.round(np.linalg.det(matriz)))%26
    det_inv = egcd(det2, mod)[1] % mod
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

#PERMUTACIÓN
import math

def permutacionCifrar(msg,key):
    cipher = ""
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    # calcular columnas de la matriz
    col = len(key)
      
    # calcular maximo filas de la matriz
    row = int(math.ceil(msg_len / col))

    # llenar de '_' a lo que falte de la matriz
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
  
    #crear la matriz con el mensaje ya separado por el tamaño de la clavee 
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
    #por cada columna leer todos sus simbolos y hacer la permutacion
    for row in matrix:
        for j in range(col):
            curr_idx = key.index(key_lst[j])
            cipher+=''.join([row[curr_idx]])
    return cipher
  
# Decryption
def permutacionDescifrar(cipher,key):
    decipher = ""
    #decipher2= ""
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    key_lst = sorted(list(key))
    # calcular columnas de la matriz
    col = len(key)
      
    # calcular maximo filas de la matriz
    row = int(math.ceil(msg_len / col))

    # llenar de '_' a lo que falte de la matriz
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
  
    #crear la matriz con el mensaje ya separado por el tamaño de la clave
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
    key2=''  # sirve para volver a la antigua permutación 
    for n in range(col):
            curr_idx = key.index(key_lst[n])
            key2+=''.join([key_lst[curr_idx]])
            
    #por cada columna leer todos sus simbolos y hacer la permutacion       
    for row in matrix:  
        for j in range(col):
            curr_idx = key2.index(key_lst[j])
            decipher+=''.join([row[curr_idx]])
 
    return decipher






















#CRIPTOANALISIS

#DESPLAZAMIENTO
def desplazamientoAnalisis(texto):
    texto.upper()
    texto=texto.replace(" ","")
    lista=list()
    for i in range(26):
        lista.append("Clave "+ str(i) + " = " + desplazamientoDescifrar(texto,i))
    return lista

#AFÍN
def affineAnalisis(texto):
    lista=list()
    clave=[0,0]
    for a in range(26):
        clave[0]=a
        if(gcd(a,26)!=0):
            for b in range(26):
                clave[1]=b
                lista.append("Clave " + "a="+str(clave[0]) + " y b=" + str(clave[1]) + " = " + affineDescifrar(texto, clave))
    return lista
         


#VIGENERE
def vigenereClave(texto):
    texto = texto.upper()
    #la primer posición corresponde a la A, la segunda a la B y así sucesivamente
    frecuencias = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #encontrando posible tamaño de la clave
    posiblesClaves = list()
    for i in range(len(texto) - 2):
        resultado=0
        tamaños = list()
        curr = texto[i:i + 3]
        for j in range(i + 3, len(texto) - 2):
            if curr == texto[j:j + 3]:
                tamaños.append(j - i)
        if len(tamaños) != 0:
            resultado=tamaños[0]
            for i in range(len(tamaños)):
                resultado=egcd(resultado,tamaños[i])[0]
        if resultado > 1 and resultado not in posiblesClaves:
            posiblesClaves.append(resultado)
    posiblesClaves.sort()

    for i in range(len(posiblesClaves)):
        if posiblesClaves[i]:
            for j in range(len(posiblesClaves)):
                if i != j:
                    if posiblesClaves[j]:
                        if egcd(posiblesClaves[j], posiblesClaves[i])[0] != 1:
                            posiblesClaves[i] = egcd(posiblesClaves[j], posiblesClaves[i])[0]
                            posiblesClaves[j] = 0
    while 0 in posiblesClaves:
        posiblesClaves.remove(0)

    #escogiendo las claves posiblemente correctas de las posibles claves
    listaClaves = []
    for m in posiblesClaves:
        subcadenas=[]
        for i in range(0,len(texto),m):
            subcadenas.append(texto[i:i+m])
        lista = list()
        suma=0
        for i in range(m):
            pal=""
            for j in subcadenas:
                if(len(j)>i):
                    pal+=j[i]
            lista.append(pal)
        for x in lista:
            suma2=0
            frequency = {u: sum([1 for r in x if u == r]) for u in letras}
            for i in letras:
                suma2=suma2 + frequency[i] * (frequency[i] - 1) / (len(x) * (len(x) - 1))
            suma=suma+suma2
        suma=float(suma)/float(len(lista))
        if abs(suma-0.065)<0.0051:
            listaClaves.append(m)

    for m in listaClaves:
        clave = list()
        subcadenas = [texto[i:i + m] for i in range(0, len(texto), m)]
        lista = list()
        for i in range(m):
            listaLetras = ""
            for j in subcadenas:
                if (len(j)>i):
                    listaLetras+=j[i]
            lista.append(listaLetras)
        for i in range(m):
            freq=[]
            for x in range(len(letras)):
                freq.append(lista[i].count(letras[x]))
            ss = []
            n = len(lista[i])
            for j in range(26):
                s = 0.0
                for k in range(26):
                    pos = (k + j) % 26
                    s += ((frecuencias[k] * freq[pos]) / float(n))
                ss.append(s)
            sLista = ss
            clave.append(sLista.index(max(sLista)))
        claveFinal=""
        for i in clave:
            claveFinal+=letras[i]
        return claveFinal

#SUSTITUCION
def counts(text):
    text.upper()
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    individuales = []
    for i in letras:
        if(not text.count(i)==0):
            individuales.append([i,text.count(i)])
    individuales.sort()


