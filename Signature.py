from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

def CrearClavesFirma():
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("private.key", "wb")
    file_out.write(private_key)
    file_out.close()
    public_key = key.publickey().export_key()
    file_out = open("public.key", "wb")
    file_out.write(public_key)
    file_out.close()

###########################################

def firmar(file):
    CrearClavesFirma()
    with open(file,"rb") as opened_file:
        f=base64.b64encode(opened_file.read())
    privatekey = RSA.import_key(open('private.key').read())
    h = SHA256.new(f)
    signer=pkcs1_15.new(privatekey)
    signature=signer.sign(h)
    file_out = open("signature.pem", "wb")
    file_out.write(signature)
    file_out.close()
    return True
    #print(signature.hex())

########################################################

def Verificar(file):
    publickey = RSA.import_key(open("public.key").read())
    file_in = open(file, "rb")
    with file_in as opened_file:
        message=base64.b64encode(opened_file.read())
    file_in.close()
    file_in = open("signature.pem", "rb")
    signature=file_in.read()
    file_in.close()
    h = SHA256.new(message)
    try:
        pkcs1_15.new(publickey).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False