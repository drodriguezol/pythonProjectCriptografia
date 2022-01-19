import math
import random

p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p4_table = [2, 4, 3, 1]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
expansion = [4, 1, 2, 3, 2, 3, 4, 1]
s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]] 


def SdesCifrar(text, key, mode):
    if(key==""):
        for i in range(10):
            key+=str(random.randint(0, 1))

    keys = GeneratedKey(key)

    file_out = open("key.txt", "w")
    file_out.write(key)
    file_out.close()

    textCript=None
    if(mode == 'ECB'):
        return S_DES_ENCRYPT_ECB(text, keys)
    elif(mode == 'CBC'):
        textCript, ivk = S_DES_ENCRYPT_CBC(text, keys)
    elif(mode == 'CFB'):
        textCript, ivk = S_DES_ENCRYPT_CFB(text, keys)
    elif(mode == 'OFB'):
        textCript, ivk = S_DES_ENCRYPT_OFB(text, keys)

    file_out = open("ivk.txt", "w")
    file_out.write(ivk)
    file_out.close()
    return textCript



def SdesDescifrar(text, key, mode):
    if(key == ""):
        file_in = open("key.txt", "r")
        key = file_in.read()
        file_in.close()
    keys = GeneratedKey(key)

    if(mode == 'ECB'):
        return S_DES_DESENCRYPT_ECB(text, keys)
    else:
        file_in = open("ivk.txt", "r")
        ivk = file_in.read()
        file_in.close()
        textCript = None
        if(mode == 'CBC'):
            textCript = S_DES_DESENCRYPT_CBC(text, keys,ivk)
        elif(mode == 'CFB'):
            textCript = S_DES_DESENCRYPT_CFB(text, keys,ivk)
        elif(mode == 'OFB'):
            textCript = S_DES_DESENCRYPT_OFB(text, keys,ivk)
        return textCript


def apply_table(inp, table):
    #pa las permutaciones
    res = ""
    for i in table:
        res += inp[i - 1]
    return res


def left_shift(data):
   # pa mover a la izquierda
    return data[1:] + data[0]


def XOR(a, b):
    res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    return res


def apply_sbox(s, data):
    row = int("0b" + data[0] + data[-1], 2)
    col = int("0b" + data[1:3], 2)
    return bin(s[row][col])[2:]


def function(expansion, s0, s1, key, message):
    left = message[:4]
    right = message[4:]
    temp = apply_table(right, expansion)
    temp = XOR(temp, key)
    l = apply_sbox(s0, temp[:4])  # noqa: E741
    r = apply_sbox(s1, temp[4:])
    l = "0" * (2 - len(l)) + l  # noqa: E741
    r = "0" * (2 - len(r)) + r
    temp = apply_table(l + r, p4_table)
    temp = XOR(left, temp)
    return temp + right


def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
def toString(bits):
 n = int(bits, 2)
 return(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
 

def SDES_ENCRIPTAR(message,keys):
    message=message.replace(" ", "")
    key1=keys[0]
    key2=keys[1]
    # encryption
    temp = apply_table(message, IP)
    temp = function(expansion, s0, s1, key1, temp)
    temp = temp[4:] + temp[:4]
    temp = function(expansion, s0, s1, key2, temp)
    CT = apply_table(temp, IP_inv)
    return CT

def SDES_DESENCRIPTAR(CT,keys):
    # decryption
    key1=keys[0]
    key2=keys[1]
    temp = apply_table(CT, IP)
    temp = function(expansion, s0, s1, key2, temp)
    temp = temp[4:] + temp[:4]
    temp = function(expansion, s0, s1, key1, temp)
    PT = apply_table(temp, IP_inv)
    return PT

def GeneratedKey(key):
    temp = apply_table(key, p10_table)
    left = temp[:5]
    right = temp[5:]
    left = left_shift(left)
    right = left_shift(right)
    key1 = apply_table(left + right, p8_table)
    left = left_shift(left)
    right = left_shift(right)
    left = left_shift(left)
    right = left_shift(right)
    key2 = apply_table(left + right, p8_table)
    keys=[key1,key2]
    return keys

def S_DES_ENCRYPT_ECB(message,keys):
  TextoEncriptado=[]
  message2=toBinary(message)
  for i in range(len(message2)):
    while(len(str(message2[i]))!=8):
     message2[i]=("0"+str(message2[i]))
    TextoEncriptado.append(SDES_ENCRIPTAR(str(message2[i]),keys))
  return(TextoEncriptado)

def S_DES_DESENCRYPT_ECB(TextoEncriptado,keys):
  plaintexto=''
  for i in range(len(TextoEncriptado)):
   plaintextobinary=SDES_DESENCRIPTAR(TextoEncriptado[i],keys)
   plaintexto=toString(plaintextobinary)+plaintexto
  return(plaintexto[::-1])

def S_DES_ENCRYPT_CBC(message,keys):
  IV=''
  for i in range(8):
     IV=str(random.randint(0, 1))+IV
  TextoEncriptado=[]
  message3=toBinary(message)
  while(len(str(message3[0]))!=8):
     message3[0]=("0"+str(message3[0]))
  message3[0]=XOR(str(message3[0]),IV)
  for i in range(len(message3)):
    if(i>0):
     while(len(str(message3[i]))!=8):
      message3[i]=("0"+str(message3[i]))
     TextoEncriptado.append(SDES_ENCRIPTAR(XOR((str(message3[i])),TextoEncriptado[i-1]),keys))
    elif(i==0):
      TextoEncriptado.append(SDES_ENCRIPTAR((str(message3[i])),keys))
  return TextoEncriptado,IV

def S_DES_DESENCRYPT_CBC(TextoEncriptado,keys,IV):
  plaintexto=''
  for i in range(len(TextoEncriptado)):
    if(i==0):
     plaintextobinary=XOR(SDES_DESENCRIPTAR(TextoEncriptado[i],keys),IV)
     plaintexto=toString(plaintextobinary)+plaintexto
    else:
     plaintextobinary=XOR(SDES_DESENCRIPTAR(TextoEncriptado[i],keys),TextoEncriptado[i-1])
     plaintexto=toString(plaintextobinary)+plaintexto
  return(plaintexto[::-1])

def S_DES_ENCRYPT_CFB(message,keys):
  VI=''
  for i in range(8):
     VI=str(random.randint(0, 1))+VI
  message4=toBinary(message)
  TextoEncriptado=[]
  for i in range(len(message4)):
    if(i==0):
        while(len(str(message4[0]))!=8):
          message4[0]=("0"+str(message4[i]))
        TextoEncriptado.append(XOR((SDES_ENCRIPTAR(VI,keys)),str(message4[0])))
    else:
        while(len(str(message4[i]))!=8):
           message4[i]=("0"+str(message4[i]))
        TextoEncriptado.append(XOR(SDES_ENCRIPTAR(TextoEncriptado[i-1],keys),str(message4[i])))
  return(TextoEncriptado,VI)

def S_DES_DESENCRYPT_CFB(TextoEncriptado,keys,VI):
  plaintexto=''
  for i in range(len(TextoEncriptado)):
    if(i==0):
      letraEncriptada=SDES_ENCRIPTAR(VI,keys)
      plaintextobinary=XOR(letraEncriptada,TextoEncriptado[0])
      plaintexto=toString(plaintextobinary)
    else:
       plaintextobinary=XOR(SDES_ENCRIPTAR(TextoEncriptado[i-1],keys),TextoEncriptado[i])
       plaintexto=toString(plaintextobinary)+plaintexto
  return(plaintexto[::-1])

def S_DES_ENCRYPT_OFB(message,keys):
  VI=''
  for i in range(8):
     VI=str(random.randint(0, 1))+VI
  message4=toBinary(message)
  TextoEncriptado=[]
  Cifrado_anterior=[]
  for i in range(len(message4)):
    if(i==0):
        while(len(str(message4[0]))!=8):
          message4[0]=("0"+str(message4[i]))
        cifrado=SDES_ENCRIPTAR(VI,keys)
        Cifrado_anterior.append(cifrado)
        TextoEncriptado.append(XOR(cifrado,str(message4[0])))
    else:
        while(len(str(message4[i]))!=8):
           message4[i]=("0"+str(message4[i]))
        cifrado=SDES_ENCRIPTAR(Cifrado_anterior[i-1],keys)
        Cifrado_anterior.append(cifrado)
        TextoEncriptado.append(XOR(cifrado,str(message4[i])))
  return(TextoEncriptado,VI)

def S_DES_DESENCRYPT_OFB(TextoEncriptado,keys,VI):
  plaintexto=''
  cifrado_anterior=[]
  for i in range(len(TextoEncriptado)):
    if(i==0):
      letraEncriptada=SDES_ENCRIPTAR(VI,keys)
      cifrado_anterior.append(letraEncriptada)
      plaintextobinary=XOR(letraEncriptada,TextoEncriptado[0])
      plaintexto=toString(plaintextobinary)
    else:
       cifrado1=SDES_ENCRIPTAR(cifrado_anterior[i-1],keys)
       cifrado_anterior.append(cifrado1)
       plaintextobinary=XOR(cifrado1,TextoEncriptado[i])
       plaintexto=toString(plaintextobinary)+plaintexto
  return(plaintexto[::-1])







from PIL import Image
import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from base64 import b64encode
import imageio as iio
import requests

def loadImageBlock(url):
    f = open('imagen.bmp', 'wb')
    f.write(requests.get(url).content)
    f.close()
    image = iio.imread('imagen.bmp')
    im = Image.fromarray(image)
    im = im.convert('RGB')
    im.save("imagen.bmp")

def loadImage2Block(a):
    if(a==0):
        image = iio.imread('imagen.bmp')
    elif(a==1):
        image = iio.imread('imagenCifrada.bmp')
    reshape = 1
    for i in image.shape:
        reshape *= i
    return image.reshape((1, reshape)), image.shape

def loadImage3Block(path):
    image = iio.imread(path)
    im = Image.fromarray(image)
    im = im.convert('RGB')
    im.save("imagen.bmp")


def AesCifrar(mode, key, bt):
    if(key==""):
        key = get_random_bytes(bt)
    ivk = get_random_bytes(16)

    if(mode == 'ECB'):
        mod = AES.MODE_ECB
    elif(mode == 'CBC'):
        mod = AES.MODE_CBC
    elif(mode == 'CFB'):
        mod = AES.MODE_CFB
    elif(mode == 'OFB'):
        mod = AES.MODE_OFB

    image = Image.open("imagen.bmp")
    size = image.size
    image = np.array(image)
    cipher = None
    if(mod != AES.MODE_ECB):
        cipher = AES.new(key, mod,iv=ivk)
    else:
        cipher = AES.new(key, mod)
    cripbytes = cipher.encrypt(pad(image.tobytes(),AES.block_size))
    imgData = np.frombuffer(cripbytes)
    im = Image.frombuffer("RGB", size, imgData)
    im.save("imagenCifrada.bmp")

    file_out = open("key.txt", "wb")
    file_out.write(key)
    file_out.close()

    file_out = open("ivk.txt", "wb")
    file_out.write(ivk)
    file_out.close()


def AesDescifrar(mode, key, bt):
    if(mode == 'ECB'):
        mod = AES.MODE_ECB
    elif(mode == 'CBC'):
        mod = AES.MODE_CBC
    elif(mode == 'CFB'):
        mod = AES.MODE_CFB
    elif(mode == 'OFB'):
        mod = AES.MODE_OFB

    if(key == ""):
        file_in = open("key.txt", "rb")
        key = file_in.read()
        file_in.close()

    file_in = open("ivk.txt", "rb")
    ivk = file_in.read()
    file_in.close()

    image = Image.open("imagenCifrada.bmp")
    size = image.size
    image = np.array(image)
        
    cipher = None
    if(mod != AES.MODE_ECB):
        cipher = AES.new(key, mod, iv=ivk)
    else:
        cipher = AES.new(key, mod)

    imagebytes = image.tobytes()
    decrypbytes = cipher.decrypt(imagebytes)
    imgData = np.frombuffer(decrypbytes)
    Image.frombuffer("RGB", size, imgData).save("imagen.bmp")


from Crypto.Cipher import DES

def DesCifrar(mode, key):
    if(key==""):
        key = get_random_bytes(8)
    ivk = get_random_bytes(8)

    if(mode == 'ECB'):
        mod = DES.MODE_ECB
    elif(mode == 'CBC'):
        mod = DES.MODE_CBC
    elif(mode == 'CFB'):
        mod = DES.MODE_CFB
    elif(mode == 'OFB'):
        mod = DES.MODE_OFB

    image = Image.open("imagen.bmp")
    size = image.size
    image = np.array(image)
    cipher = None
    if(mod != DES.MODE_ECB):
        cipher = DES.new(key, mod,iv=ivk)
    else:
        cipher = DES.new(key, mod)
    cripbytes = cipher.encrypt(pad(image.tobytes(), DES.block_size))
    imgData = np.frombuffer(cripbytes)
    im = Image.frombuffer("RGB", size, imgData)
    im.save("imagenCifrada.bmp")
        
    file_out = open("key.txt", "wb")
    file_out.write(key)
    file_out.close()

    file_out = open("ivk.txt", "wb")
    file_out.write(ivk)
    file_out.close()


def DesDescifrar(mode, key):
    if(mode == 'ECB'):
        mod = DES.MODE_ECB
    elif(mode == 'CBC'):
        mod = DES.MODE_CBC
    elif(mode == 'CFB'):
        mod = DES.MODE_CFB
    elif(mode == 'OFB'):
        mod = DES.MODE_OFB

    if(key == ""):
        file_in = open("key.txt", "rb")
        key = file_in.read()
        file_in.close()

    file_in = open("ivk.txt", "rb")
    ivk = file_in.read()
    file_in.close()

    image = Image.open("imagenCifrada.bmp")
    size = image.size
    image = np.array(image)
        
    cipher = None
    if(mod != DES.MODE_ECB):
        cipher = DES.new(key, mod, iv=ivk)
    else:
        cipher = DES.new(key, mod)

    imagebytes = image.tobytes()
    decrypbytes = cipher.decrypt(imagebytes)
    imgData = np.frombuffer(decrypbytes)
    Image.frombuffer("RGB", size, imgData).save("imagen.bmp")

from Crypto.Cipher import DES3

def Des3Cifrar(mode, key):
    if(key==""):
        key = get_random_bytes(24)
    ivk = get_random_bytes(8)

    if(mode == 'ECB'):
        mod = DES3.MODE_ECB
    elif(mode == 'CBC'):
        mod = DES3.MODE_CBC
    elif(mode == 'CFB'):
        mod = DES3.MODE_CFB
    elif(mode == 'OFB'):
        mod = DES3.MODE_OFB

    image = Image.open("imagen.bmp")
    size = image.size
    image = np.array(image)
    cipher = None
    if(mod != DES3.MODE_ECB):
        cipher = DES3.new(key, mod, ivk)
    else:
        cipher = DES3.new(key, mod)
    cripbytes = cipher.encrypt(pad(image.tobytes(), DES3.block_size))
    imgData = np.frombuffer(cripbytes)
    im = Image.frombuffer("RGB", size, imgData)
    im.save("imagenCifrada.bmp")
        
    file_out = open("key.txt", "wb")
    file_out.write(key)
    file_out.close()

    file_out = open("ivk.txt", "wb")
    file_out.write(ivk)
    file_out.close()


def Des3Descifrar(mode, key):
    if(mode == 'ECB'):
        mod = DES3.MODE_ECB
    elif(mode == 'CBC'):
        mod = DES3.MODE_CBC
    elif(mode == 'CFB'):
        mod = DES3.MODE_CFB
    elif(mode == 'OFB'):
        mod = DES3.MODE_OFB

    if(key == ""):
        file_in = open("key.txt", "rb")
        key = file_in.read()
        file_in.close()

    #ivk = get_random_bytes(8)
    file_in = open("ivk.txt", "rb")
    ivk = file_in.read()
    file_in.close()

    image = Image.open("imagenCifrada.bmp")
    size = image.size
    image = np.array(image)
        
    cipher = None
    if(mod != DES3.MODE_ECB):
        cipher = DES3.new(key, mod, iv=ivk)
    else:
        cipher = DES3.new(key, mod)

    imagebytes = image.tobytes()
    decrypbytes = cipher.decrypt(imagebytes)
    imgData = np.frombuffer(decrypbytes)
    Image.frombuffer("RGB", size, imgData).save("imagen.bmp")
