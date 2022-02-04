from sympy import randprime, isprime
import random
import math


def generatePrime(a=0):
    if a!=0:
        return randprime(2**(a-2),2**(a-1))
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
    key= random.randint(0,p)
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

def generateGamalData(p, alpha=0):
    if alpha==0:
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







#MV
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r
def ec_gen_points_set(a, b, p):
    ec_points_on_curve = []
    for x in range(p):
        y2 = x ** 3 + a * x + b
        lengdre_val = legendre(y2, p)
        if lengdre_val != 0:
            if lengdre_val != 1:  # (y2 | p) must be ≡ 1 to have a square if not continue to next num
                continue
        elif lengdre_val == 0:
            y_root1 = 0
            gen1 = (x, y_root1)
            ec_points_on_curve.append(gen1)
            continue
        y_root1 = tonelli(y2, p)  # one possible root
        y_root2 = p - y_root1

        if y_root2 < y_root1:
            gen1 = (x, y_root2)
            gen2 = (x, y_root1)
        else:
            gen1 = (x, y_root1)
            gen2 = (x, y_root2)

        ec_points_on_curve.append(gen1)
        ec_points_on_curve.append(gen2)
    return ec_points_on_curve

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


# calculate `modular inverse`
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g == 1:
        return x % m
    else:
        return None

#OPERACIONES ECC
# double function
def ecc_double(x1, y1, p, a):
    if modinv(2 * y1, p) is None: return None

    s = ((3 * (x1 ** 2) + a) * modinv(2 * y1, p)) % p
    x3 = (s ** 2 - x1 - x1) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)


# add function
def ecc_add(x1, y1, x2, y2, p, a):
    s = 0
    if (x1 == x2):
        if modinv(2 * y1, p) is None : return None
        s = ((3 * (x1 ** 2) + a) * modinv(2 * y1, p)) % p
    else:
        if modinv(x2 - x1, p) is None: return None
        s = ((y2 - y1) * modinv(x2 - x1, p)) % p
    x3 = (s ** 2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)


def double_and_add(multi, generator, p, a):
    (x3, y3) = (0, 0)
    (x1, y1) = generator
    (x_tmp, y_tmp) = generator
    init = 0
    for i in str(bin(multi)[2:]):
        if (i == '1') and (init == 0):
            init = 1
        elif (i == '1') and (init == 1):
            if ecc_double(x_tmp, y_tmp, p, a) is None: return None
            if ecc_add(x1, y1, x3, y3, p, a) is None: return None
            (x3, y3) = ecc_double(x_tmp, y_tmp, p, a)
            (x3, y3) = ecc_add(x1, y1, x3, y3, p, a)
            (x_tmp, y_tmp) = (x3, y3)
        else:
            if ecc_double(x_tmp, y_tmp, p, a) is None: return None
            (x3, y3) = ecc_double(x_tmp, y_tmp, p, a)
            (x_tmp, y_tmp) = (x3, y3)
    return (x3, y3)


def scale_point_set(a, b, p, generator):
    ec_curve_points = ec_gen_points_set(a, b, p)
    scaled_points_set = {}
    i = 1
    scaled_points_set[str(i) + "P"] = generator

    while True:
        i += 1
        scaled_point = double_and_add(i, generator, p, a)

        if scaled_point is None or scaled_point not in ec_curve_points:
            scaled_points_set[str(i) + "P"] = "O"
            break

        elif scaled_point in ec_curve_points:
            scaled_points_set[str(i) + "P"] = scaled_point
            if str(i) + "P" != "2P" and scaled_points_set["2P"] == scaled_points_set[str(i) + "P"]:  # the current index is not 2P and no other duplicate point exists
                scaled_points_set[str(i) + "P"] = "O"
                break    #if duplicate P exists then stop

    return scaled_points_set
def KeyGen(key, pointSet):
    order = len(pointSet)
    if key > order:
        key = key % order

        if key == 0: return pointSet[str(order) + "P"]  # if the modulo is zero return the last element in list

        key = pointSet[str(key) + "P"]  # User Public Key
    else:
        key = pointSet[str(key) + "P"]  # User Public Key

    return key

# agoritmo extendido de euclides que toma 2 primos relativos y les encuentra inverso modular
def Inverse_Mod(e, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (e > 1):
        q = int(e / m)  # q is quotient
        temp = m
        m = e % m
        e = temp
        temp = y
        # Update x and y
        y = x - q * y
        x = temp
    # Make x positive
    if (x < 0): x = x + m0
    return x
def primitivo(a,b,p):
	for x in range(1,p):
		val=((x*x*x)+a*x+b) % p
		res = math.sqrt(val)
		if (abs(res-int(res))<0.0001):
			return(x,int(res))

def CifrarMenezesVastone(a,b,p,gx,gy,Ka,Nb,text):
  cifrado=[]
  generator=(gx,gy)
  y0 = KeyGen(Ka, scale_point_set(a, b, p, generator))
  publicKeyB = KeyGen(Nb, scale_point_set(a, b, p, generator))
  mask = KeyGen(Ka, scale_point_set(a, b, p, publicKeyB))
  for i in range(len(text)):
   m=str(ord(text[i]))
   if((len(m)%2)!=0):
      m1 = int(m[:(len(m)//2)+1])
      m2 = int(m[len(m)//2+1:])
   else:
      m1 = int(m[:(len(m)//2)])
      m2 = int(m[len(m)//2:])
   y1 = (mask[0]*m1)%p
   y2 = (mask[1]*m2)%p
   cifrado.append((y0,y1,y2))
  #print("(C1,C2)):", mask)
  return(cifrado)
def DecifradoMenezesVastone(a,b,p,Nb,tcifrado):
  TextoDecifrado=""
  for i in range(len(tcifrado)):
   Nb_hint= KeyGen(Nb, scale_point_set(a, b, p, tcifrado[i][0]))
   inv_c1 = Inverse_Mod(Nb_hint[0],p)
   decrypt_m1 = (inv_c1*tcifrado[i][1])%p
   inv_c2 = Inverse_Mod(Nb_hint[1],p)
   decrypt_m2 = (inv_c2*tcifrado[i][2])%p
   TextoDecifrado = TextoDecifrado + chr(int(str(decrypt_m1) + str(decrypt_m2)))
  return TextoDecifrado

def generateDataMV(p):
    if p=="":
        p=randprime(100,1000)
    else:
        p=int(p)
    a=random.randint(0,100)
    b=random.randint(0,100)
    gx,gy=primitivo(a,b,p)
    ca=random.randint(10**2,10**3)
    while(ca>p):
        ca=random.randint(10**2,10**3)
    cb=random.randint(10**2,10**3)
    while(cb>p):
        cb=random.randint(10**2,10**3)
    file_out = open("public_key.txt", "w")
    file_out.write(str(a))
    file_out.write("\n")
    file_out.write(str(b))
    file_out.write("\n")
    file_out.write(str(p))
    file_out.write("\n")
    file_out.write(str(gx))
    file_out.write("\n")
    file_out.write(str(gy))
    file_out.write("\n")
    file_out.write(str(cb))
    file_out.close()

    file_out = open("private_key.txt", "w")
    file_out.write(str(ca))
    file_out.close()
    return a,b,p,gx, gy, ca, cb




#RABIN
import random
import sys

from Crypto.Util.number import *
import codecs
import Crypto
from Crypto import Random


def cifrarRabin(plaintext):
    file_in = open("public_key.txt", "r")
    n = int(file_in.read())
    file_in.close()
    plaintext = bytes_to_long(plaintext.encode('utf-8'))
    # c = m^2 mod n
    plaintext = padding(plaintext)
    return plaintext ** 2 % n


def padding(plaintext):
    binary_str = bin(plaintext)  # convert to a bit string
    output = binary_str + binary_str[-16:]  # pad the last 16 bits to the end
    return int(output, 2)  # convert back to integer


def decifrarRabin(a):
    file_in = open("private_key.txt", "r")
    p = int(file_in.readline().rstrip())
    q = int(file_in.readline().rstrip())
    file_in.close()
    file_in = open("public_key.txt", "r")
    n = int(file_in.read())
    file_in.close()
    r, s = 0, 0
    # find sqrt
    # for p
    if p % 4 == 3:
        r = sqrt_p_3_mod_4(a, p)
    elif p % 8 == 5:
        r = sqrt_p_5_mod_8(a, p)
    # for q
    if q % 4 == 3:
        s = sqrt_p_3_mod_4(a, q)
    elif q % 8 == 5:
        s = sqrt_p_5_mod_8(a, q)

    gcd, c, d = egcd(p, q)
    x = (r * d * q + s * c * p) % n
    y = (r * d * q - s * c * p) % n
    lst = [x, n - x, y, n - y]
    plaintext = choose(lst)

    string = bin(plaintext)
    string = string[:-16]
    plaintext = int(string, 2)

    return plaintext


# decide which answer to choose
def choose(lst):
    for i in lst:
        binary = bin(i)

        append = binary[-16:]  # take the last 16 bits
        binary = binary[:-16]  # remove the last 16 bits

        if append == binary[-16:]:
            return i
    return


# Find SQROOT in Zp where p = 3 mod 4
def sqrt_p_3_mod_4(a, p):
    r = pow(a, (p + 1) // 4, p)
    return r


# Find SQROOT in Zp where p = 5 mod 8
def sqrt_p_5_mod_8(a, p):
    d = pow(a, (p - 1) // 4, p)
    r = 0
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
    elif d == p - 1:
        r = 2 * a * pow(4 * a, (p - 5) // 8, p) % p

    return r


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, y, x = egcd(b % a, a)
        return gcd, x - (b // a) * y, y

def generateDataRabin():
    bits=524
    while True:
        p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
        if ((p % 4) == 3): break

    while True:
        q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
        if ((p % 4) == 3): break
    file_out = open("public_key.txt", "w")
    file_out.write(str(p*q))
    file_out.close()
    file_out = open("private_key.txt", "w")
    file_out.write(str(p))
    file_out.write("\n")
    file_out.write(str(q))
    file_out.close()
    return p,q