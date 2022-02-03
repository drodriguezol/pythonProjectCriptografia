import hashlib
from PublicKey import*

def hashSign(filename):
    with open(filename, 'rb') as opened_file:
        file= opened_file.read()
        hash= hashlib.sha224()
        hash.update(file)
    return hash.hexdigest()

def signature(filename, p, alpha, alpha_a):
    ciph= ElgamalCifrar(hashSign(filename),p,alpha_a,alpha)
    file_out = open("signature.txt", "w")
    file_out.write(str(ciph))
    file_out.close()


def check(filename):
    M = hashSign(filename)
    file_in = open("ak.txt", "r")
    S1 = int(file_in.read())
    file_in.close()
    file_in = open("signature.txt", "r")
    S2 = file_in.read()
    file_in.close()
    file_in = open("public_key.txt", "r")
    p = int(file_in.readline().rstrip())
    e1 = int(file_in.readline().rstrip())
    e2 = int(file_in.readline().rstrip())
    file_in.close()
    V1=pow(e1,M)
    V1=V1%p
    V2=pow(e2,S1)*pow(S1,S2)
    V2=V2%p
    if V1==V2:
        return True
    else:
        return False


