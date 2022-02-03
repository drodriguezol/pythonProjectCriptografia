from sympy import randprime
import random


def generatePrime():
    return randprime(2**(256),2**(512))

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def generateRsaData(p,q):
    n=p*q
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    #for i in range(2,phi):
    #    if(gcd(i,phi)==1 and gcd(i,n)==1):
    pub_key=e
            #break
    file_out = open("pub_key.txt", "w")
    file_out.write(str(pub_key))
    file_out.close()
    # Private key generation
    d = 0
    d =multiplicative_inverse(pub_key,phi)
    #while d < 1:
    #    if (pub_key * d) % phi == 1:
    #        break
    #    d = d+1
    priv_key = d
    file_out = open("priv_key.txt", "w")
    file_out.write(str(priv_key))
    file_out.close()
    return (pub_key, n)

def RsaCifrar(message, p, q):
    n=p*q
    file_in = open("pub_key.txt", "r")
    pub_key = int(file_in.read())
    file_in.close()
    encrypt_text = []
    for letter in message:
        m = ord(letter)
        cipher_text = pow(m,pub_key,n)#(m**pub_key)%n
        encrypt_text.append(str(cipher_text))
    return(encrypt_text)

def RsaDescifrar(message, p, q):
    n=p*q
    file_in = open("priv_key.txt", "r")
    priv_key = int(file_in.read())
    file_in.close()
    decrypt_text = ""
    for letter in message:
        c = int(letter)
        decrypt_letter = pow(c,priv_key,n)#(c**priv_key)%n
        ascii_convert = chr(decrypt_letter)
        decrypt_text = decrypt_text + ascii_convert
    return(decrypt_text)


def multiplicative_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi


#Elgamal
#For key generation i.e. large random number
def gen_key(p):
    key= random.randint(pow(10,20),p)
    while gcd(p,key)!=1:
        key=random.randint(0,p)
    return key
def exp_modular(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c
        y=(y*y)%c
        b=int(b/2)
    return x%c
#For asymetric encryption
def ElgamalCifrar(msg,p,h,g):
    ct=[]
    key=gen_key(p)
    a_k=exp_modular(g,key,p)
    a_k_k=exp_modular(h,key,p)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    for i in range(0,len(ct)):
        ct[i]=str(a_k_k*ord(ct[i]))
    file_out = open("ak.txt", "w")
    file_out.write(str(a_k))
    file_out.close()
    return ct
#For decryption
def ElgamalDescifrar(ct):
    file_in = open("ak.txt", "r")
    a_k = int(file_in.read())
    file_in.close()
    file_in = open("public_key.txt", "r")
    p = int(file_in.readline().rstrip())
    file_in.close()
    file_in = open("private_key.txt", "r")
    key = int(file_in.read())
    file_in.close()
    #p=int(file1.readline().rstrip())
    pt=[]
    h=exp_modular(a_k,key,p)
    for i in range(0,len(ct)):
        pt.append(chr(int(int(ct[i])/h)))
    return pt

def generateGamalData(p):
    alpha=random.randint(2,p) #generador
    a=gen_key(p) # clave privada
    alpha_a=exp_modular(alpha,a,p) #alpha^a
    file_out = open("public_key.txt", "w")
    file_out.write(str(p))
    file_out.write("\n")
    file_out.write(str(alpha))
    file_out.write("\n")
    file_out.write(str(alpha_a))
    file_out.close()
    file_out = open("private_key.txt", "w")
    file_out.write(str(a))
    file_out.close()
    return alpha, a, alpha_a