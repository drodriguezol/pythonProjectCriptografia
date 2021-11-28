#Funciones de criptación y desencriptación

#DESPLAZMIENTO CIPHER
def desplazamientoCifrar(text,s):
    text=text.replace(" ","")
    text=text.upper()
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        result += chr(((ord(char) + s-65) % 26)+65)
    return result

def desplazamientoDescifrar(text,s):
    text=text.replace(" ","")
    text.upper()
    result=""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) -(s-65)) % 26 +65 )
    return result

'''
n="Solo ingresa letras, vuelve a intentarlo!"
while not text.isalpha():#verificar que el texto sea solo string
  print(n)
  text_input=str(input())
  text=text_input.replace(" ","")
while True: #verificar que la clave sea un número entero
 try:
  s=int(input("escribe la clave :"))
  break;
 except:
   print("por favor escribe un número entero")

#print ("Text  : " + text)
#print ("Shift : " + str(s))
h=str(input("escribe cifrar o decifrar: "))
if(h=="cifrar"):
 print ("texto cifrado: " + cifrar(text,s))
elif(h=="decifrar"):
  print ("texto cifrado: " + decifrar(text,s))
  '''