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
    else:
        print("Mode not recognized")
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
    else:
        print("Mode not recognized")
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
        ivk = get_random_bytes(8)
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
    else:
        print("Mode not recognized")
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
