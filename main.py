#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from cgitb import text
from os import stat
from tkinter import ttk
from tkinter import *
from tkinter import Text, Tk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
from io import BytesIO
from tkinter.filedialog import askopenfilename
from sympy import randprime

from PublicKey import*
from Cypher import*
from Block import*
import Signature as Si
#DANIELCRACK


#REPETICIONES
#MONOGRAMAS
def frecuenciaMonogramas(text):
 text=text.upper()
 text=text.replace(" ","")
 digramas=[]
 lista_de_digramas_text=[]
 #CONVERTIR TEXTO EN TODOS LOS POSIBLES DIGRAMAS CONCATENADOS SIN ESPACIOS
 for i in range (len(text)):
    try:
     a=text[i]
     lista_de_digramas_text.append(a)
    except:
      idontusethis=0
 #DIGRAMAS AUX
 digrams=list(set(lista_de_digramas_text))

 #LISTA DE FRECUENCIA
 digramsfrecuency=[]
 for i in range(len(digrams)): 
   digramsfrecuency.append(0)
 
 #CONTADOR DE DIGRAMAS
 i=0
 for x in range(len(digrams)):
     for y in range(len(lista_de_digramas_text)):
       if(digrams[x]==lista_de_digramas_text[y]):
           i=i+1
           digramsfrecuency[x]=i
     i=0
 tuplas=[]
 for xi in range(len(digrams)):
     tupla=(digrams[xi],digramsfrecuency[xi])
     tuplas.append(tupla)
 tuplas_ordenadas=sorted(tuplas, key=lambda tup: tup[1],reverse=True)
 return(tuplas_ordenadas)

#DIGRAMAS
def frecuenciaDigramas(text):
 text=text.upper()
 text=text.replace(" ","")
 lista_de_digramas_text=[]
 #CONVERTIR TEXTO EN TODOS LOS POSIBLES DIGRAMAS CONCATENADOS SIN ESPACIOS
 for i in range (len(text)):
    try:
     a=text[i]+text[i+1]
     lista_de_digramas_text.append(a)
    except:
      idontusethis=0
 #DIGRAMAS AUX
 digrams=list(set(lista_de_digramas_text))

 #LISTA DE FRECUENCIA
 digramsfrecuency=[]
 for i in range(len(digrams)): 
   digramsfrecuency.append(0)
 
 #CONTADOR DE DIGRAMAS
 i=0
 for x in range(len(digrams)):
     for y in range(len(lista_de_digramas_text)):
       if(digrams[x]==lista_de_digramas_text[y]):
           i=i+1
           digramsfrecuency[x]=i
     i=0
 tuplas=[]
 for xi in range(len(digrams)):
     tupla=(digrams[xi],digramsfrecuency[xi])
     tuplas.append(tupla)
 tuplas_ordenadas=sorted(tuplas, key=lambda tup: tup[1],reverse=True)
 return(tuplas_ordenadas)


#TRIGRAMAS
def frecuenciaTrigramas(text): 
  text=text.upper()
  text=text.replace(" ","")
  #trigrams=['the', 'and', 'tha', 'ent', 'ing', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men']
  trigrams=[]
  lista_de_trigramas_text=[]
  #CONVERTIR TEXTO EN TODOS LOS POSIBLES DIGRAMAS CONCATENADOS SIN ESPACIOS
  for i in range (len(text)):
     try:
      a=text[i]+text[i+1]+text[i+2]
      lista_de_trigramas_text.append(a) 
     except:
        #print(lista_de_trigramas_text)
        idontusethis=0
  #LISTA DE FRECUENCIA
  trigrams=list(set(lista_de_trigramas_text))
  trigramsfrecuency=[]
  for i in range(len(trigrams)): 
    trigramsfrecuency.append(0)
  text=text.replace(" ","")
  #CONTADOR DE TRIGRAMAS
  i=0
  for x in range(len(trigrams)):
      for y in range(len(lista_de_trigramas_text)):
        if(trigrams[x]==lista_de_trigramas_text[y]):
            i=i+1
            trigramsfrecuency[x]=i
      i=0
  tuplas=[]
  for xi in range(len(trigrams)):
     tupla=(trigrams[xi],trigramsfrecuency[xi])
     tuplas.append(tupla)
  tuplas_ordenadas=sorted(tuplas, key=lambda tup: tup[1],reverse=True)
  return(tuplas_ordenadas)



class CriptoSistemas(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        global mainWindow
        mainWindow=main_window
        mainWindow.iconbitmap('moon.ico')
        mainWindow.resizable(0, 0)
        main_window.title("Criptosistemas Cl??sicos")
        main_window.configure(width=1400, height=500,bg="black")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.image1 = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrame = LabelFrame(self)
        imageLabelFrame.place(x=0, y=0)
        imageLabelFrame.configure(width=1400, height=1000)
        imageLabel = Label(imageLabelFrame, image=self.image1)
        imageLabel.place(x=200, y=200, anchor="center")
        self.place(width=1400, height=500)

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5,bg="black",fg="white")
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5,bg='black',fg='white')
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Desplazamiento", "Af??n", "Vigenere", "Sustituci??n","Hill","Permutaci??n", "Hill para Imagen"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)
        claveLabel = Label(opcionesCifrado, text="Clave: ", padx=5, pady=5,bg="black",fg="white")
        claveLabel.grid(row=1, column=0)

        clave=Text(opcionesCifrado)
        clave.grid(row=1,column=1, sticky=W)
        clave.configure(height=1,width=16, padx=5, pady=5)

        cifrarFrame = LabelFrame(self, text="Cifrar",bg='black',fg='white')
        cifrarFrame.place(x=30, y=180)

        ctClaro = Label(cifrarFrame, text="Texto",bg='black',fg='white',font=('Arial',15))
        ctClaro.grid(row=0, sticky=W)

        ctCifrado = Label(cifrarFrame, text="Resultado",bg='black',fg='white')
        ctCifrado.grid(row=0, column=1, sticky=W, padx=4, pady=2)

        texto=Text(cifrarFrame)
        texto.grid(row=1,column=0, padx=4, pady=2)
        texto.configure(height=10,width=25, bg="light yellow", foreground="#000000")

        resultado=Text(cifrarFrame)
        resultado.grid(row=1,column=1, padx=4, pady=2)
        resultado.configure(height=10,width=25, bg="light cyan", foreground="#000000", state="disabled")


        #funciones para los botones
        def cifrar():
            text=texto.get("1.0","end-1c").replace(" ","").replace("\n","")
            password=clave.get("1.0","end-1c").replace(" ","")
            boolPass=True

            if (not text.isalpha()) and not text.split(" ")==['']:
                    messagebox.showinfo("Advertencia","S??lo se admiten letras en el texto.")
                    main_window.deiconify()

            elif(self.combo.get())=='Desplazamiento': 
                try:
                    password=(int(password))
                    if (password<0):
                        boolPass=False
                except:
                    boolPass=False
                if(not boolPass):
                    messagebox.showinfo("Advertencia","S??lo se admiten n??meros naturales como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, desplazamientoCifrar(text,password))
                    resultado.configure(state='disabled')
                
            elif (self.combo.get())=="Af??n" :
                password=password.split(",")
                if(len(password)>2):
                    boolPass=False
                try:
                    password[0]=(int(password[0]))
                    if (password[0]<0):
                        boolPass=False
                    password[1]=(int(password[1]))
                    if (password[1]<0):
                        boolPass=False
                except:
                    boolPass=False

                if(not boolPass):
                    messagebox.showinfo("Advertencia","Hay un error con la clave. Digite los dos n??meros separados por una coma (',').")
                    main_window.deiconify()
                else:
                    insert=affineCifrar(text,password)
                    if(insert==0):
                         messagebox.showinfo("Advertencia","El mcd de " + str(password[0]) + " y 26 no es 1, intenta con otra clave.")
                         main_window.deiconify()
                    else:
                        resultado.configure(state='normal')
                        resultado.delete("1.0", END)
                        resultado.insert(INSERT, affineCifrar(text,password))
                        resultado.configure(state='disabled')
            
            elif(self.combo.get())=='Vigenere': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","S??lo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, vigenereCifrar(text,password))
                    resultado.configure(state='disabled')

            elif(self.combo.get())=='Sustituci??n': 
                import random
                letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                if (not password.isalpha() and not password.replace(" ","")==""):
                    messagebox.showinfo("Advertencia","S??lo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    if(password==''):
                        letras = list(letras)
                        random.shuffle(letras)
                        password=''.join(letras)
                        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        clave.insert(INSERT, password)
                        messagebox.showinfo("Advertencia","La clave se ha generado autom??ticamente.")
                        main_window.deiconify()
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, sustitucionCifrar(text,password,letras))
                    resultado.configure(state='disabled')  

            elif(self.combo.get())=='Hill': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","S??lo se admiten letras como clave.")
                    main_window.deiconify()
                elif (not int((len(password)**0.5))**2 == len(password)):
                    messagebox.showinfo("Advertencia","El tama??o de la clave debe corresponder con un n??mero cuadrado perfecto.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    try:
                        resultado.insert(INSERT, hillCifrar(text,password))
                    except:
                        messagebox.showinfo("Advertencia","Hay un error con la clave. Intente nuevamente.")
                        main_window.deiconify()
                    resultado.configure(state='disabled')  

            elif(self.combo.get())=='Permutaci??n': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","S??lo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    try:
                        resultado.insert(INSERT, permutacionCifrar(text,password))
                    except:
                        messagebox.showinfo("Advertencia","Hay un error con la clave. Intente nuevamente.")
                        main_window.deiconify()
                    resultado.configure(state='disabled')                  

        def descifrar():
            text=texto.get("1.0","end-1c").replace(" ","").replace("\n","")
            password=clave.get("1.0","end-1c")
            boolPass=True
            if (not text.isalpha()) and not text.split(" ")==['']:
                    messagebox.showinfo("Advertencia", "S??lo se admiten letras en el texto.")
                    main_window.deiconify()

            if (self.combo.get())=='Desplazamiento':
                try:
                    password=(int(password))
                    if (password<0):
                        boolPass=False
                except:
                    boolPass=False
                
                if(not boolPass):
                    messagebox.showinfo("Advertencia","S??lo se admiten n??meros naturales como clave.")
                    main_window.deiconify()
                else:    
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, desplazamientoDescifrar(text,password))
                    resultado.configure(state='disabled')

            elif (self.combo.get())=="Af??n" :
                password=password.split(",")
                if(len(password)>2):
                    boolPass=False
                try:
                    password[0]=(int(password[0]))
                    if (password[0]<0):
                        boolPass=False
                    password[1]=(int(password[1]))
                    if (password[1]<0):
                        boolPass=False
                except:
                    boolPass=False

                if(not boolPass):
                    messagebox.showinfo("Advertencia","Hay un error con la clave. Digite los dos n??meros separados por una coma (',').")
                    main_window.deiconify()
                else:
                    insert=affineDescifrar(text,password)
                    if(insert==0):
                         messagebox.showinfo("Advertencia","El mcd de " + str(password[0]) + " y 26 no es 1, intenta con otra clave.")
                         main_window.deiconify()
                    else:
                        resultado.configure(state='normal')
                        resultado.delete("1.0", END)
                        resultado.insert(INSERT, affineDescifrar(text,password))
                        resultado.configure(state='disabled')

            elif(self.combo.get())=='Vigenere': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","S??lo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, vigenereDescifrar(text,password))
                    resultado.configure(state='disabled')

            elif(self.combo.get())=='Sustituci??n': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","S??lo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, sustitucionDescifrar(text,password))
                    if resultado.get("1.0", "end-1c")=="":
                        messagebox.showinfo("Hay un error con la clave. Verifique que tiene todas las letras del alfabeto sin repetirse.")
                        main_window.deiconify()
                    resultado.configure(state='disabled')

            elif(self.combo.get())=='Hill': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","S??lo se admiten letras como clave.")
                    main_window.deiconify()
                elif(not int((len(password)**(0.5))**2)-len(password)==0):
                    messagebox.showinfo("Advertencia","El tama??o de la clave debe corresponder con un n??mero cuadrado perfecto.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    try:
                        resultado.insert(INSERT, hillDescifrar(text,password))
                    except:
                        messagebox.showinfo("Advertencia","Hay un error con la clave. Intente nuevamente.")
                        main_window.deiconify()
                    resultado.configure(state='disabled')

            elif(self.combo.get())=='Permutaci??n': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","S??lo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    try:
                        resultado.insert(INSERT, permutacionDescifrar(text,password))
                    except:
                        messagebox.showinfo("Advertencia","Hay un error con la clave. Intente nuevamente.")
                        main_window.deiconify()
                    resultado.configure(state='disabled')

        def copiar_al_portapapeles():
            self.clipboard_clear()
            self.clipboard_append(resultado.get("1.0","end-1c"))

        def pegar():
            texto.delete("1.0", END)
            texto.insert(INSERT, self.clipboard_get())
        def generarclave():
            if ((self.combo.get()) == 'Desplazamiento'):
                clave.delete("1.0", END)
                clave.insert(1.0,"7")
            elif ((self.combo.get()) == 'Af??n'):
                clave.delete("1.0", END)
                clave.insert(1.0, "5,6")
            elif ((self.combo.get()) == 'Vigenere'):
                clave.delete("1.0", END)
                clave.insert(1.0, "CIPHER")
            elif ((self.combo.get()) == 'Sustituci??n'):
                clave.delete("1.0", END)
                clave.insert(1.0, "XNYAHPOGZQWBTSFLRCVMUEKJDI")
            elif ((self.combo.get()) == 'Hill'):
                clave.delete("1.0", END)
                clave.insert(1.0, "LIDH")
            elif ((self.combo.get()) == 'Permutaci??n'):
                clave.delete("1.0", END)
                clave.insert(1.0, "CFABD")

   
        def limpiar():
            resultado.configure(state='normal')
            resultado.delete("1.0", END)
            resultado.configure(state='disabled')
            texto.delete("1.0", END)

        botonesFrame = Frame(cifrarFrame, border=0,padx=5,pady=5,bg="black")
        botonesFrame.grid(row=2, column=0)

        botonesFrame2 = Frame(cifrarFrame, border=0,padx=5,pady=5,bg="black")
        botonesFrame2.grid(row=2, column=1)
        
        #espaciado entre botones
        for i in range(2):
            botonesFrame2.columnconfigure((0,i), weight=1, pad=30)
        for i in range(3):
            botonesFrame.columnconfigure((0,i), weight=1, pad=25)

        botonCifrar =Button(botonesFrame, command=cifrar, text="Cifrar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonCifrar.grid(row=0,column=0)

        botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonDescifrar.grid(row=0,column=1)  

        botonPegar =Button(botonesFrame, command=pegar, text="Pegar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonPegar.grid(row=0,column=2)       

        botonLimpiar =Button(botonesFrame2, command=limpiar, text="Limpiar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonLimpiar.grid(row=0,column=0)

        botonCopiar =Button(botonesFrame2, command=copiar_al_portapapeles, text="Copiar", padx=5, pady=5,
                            font=('Comic Sans MS', 15, 'bold'))
        botonCopiar.grid(row=0,column=1)
        
        botonGenerarClave=Button(botonesFrame2, command=generarclave, text="Generar Clave", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonGenerarClave.grid(row=0,column=3)

        instrucciones = LabelFrame(self, text="Anotaciones",bg="black",fg='white')
        instrucciones.place(x=700, y= 30)

        instruc1=Label(instrucciones, text="1. Para el cifrado de desplazamiento la clave debe ser un n??mero natural.",bg="black",fg='white')
        instruc1.grid(row=0, column=0, stick=W)

        instruc2=Label(instrucciones, text="2. Para el cifrado af??n, la clave debe componerse de dos n??meros naturales separados "
                                           "por una coma.",bg="black",fg='white')
        instruc2.grid(row=1, column=0, stick=W)

        instruc3=Label(instrucciones, text="3. Para el cifrado Vigenere, la clave debe componerse de una cadena ??nicamente "
                                           "de letras.",bg="black",fg='white')
        instruc3.grid(row=2, column=0, stick=W)
        
        instruc4 = Label(instrucciones,
                         text="4. Para el cifrado de sustituci??n, la clave es un permutacion del abecedario usual usado.",bg="black",fg='white')
        instruc4.grid(row=3, column=0, stick=W)
        
        instruc5 = Label(instrucciones,
                         text="5. Para el cifrado de hill, la clave es una palabra con tama??o cuadrado e invertible.",bg="black",fg='white')
        instruc5.grid(row=4, column=0, stick=W)
        
        instruc6 = Label(instrucciones,
                         text="6. Para el cifrado de permutaci??n, la clave es una palabra sin simbolos repetidos.",bg="black",fg='white')
        instruc6.grid(row=5, column=0, stick=W)




    def seleccion(self, event):
        if (self.combo.get()=="Hill para Imagen"):
            self = CriptoSistemasImagen(mainWindow)
            self.combo.current(6)



class CriptoSistemasImagen(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Criptosistemas Cl??sicos")
        main_window.configure(width=1200, height=750,bg='black')
        main_window.iconbitmap('moon.ico')
        main_window.resizable(0, 0)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1200, height=1200)
        self.imagespace = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrames = LabelFrame(self)
        imageLabelFrames.place(x=0, y=0)
        imageLabelFrames.configure(width=1200, height=1000)
        imageLabels = Label(imageLabelFrames, image=self.imagespace)
        imageLabels.place(x=200, y=200, anchor="center")

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5,bg='black',fg='white')
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5,bg='black',fg='white')
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Desplazamiento", "Af??n", "Vigenere", "Sustituci??n","Hill","Permutaci??n", "Hill para Imagen"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)
        self.combo.current(6)

        labelInfo=LabelFrame(self,text="Informaci??n",bg='black',fg='white')
        labelInfo.place(x=320,y=30)
        labelClave = Label(labelInfo, text="Al cifrar, se generar?? autom??ticamente una clave y se guardar?? en el archivo"
                                           " key.npy dentro de la carpeta del proyecto.",bg="black",fg='white')
        labelClave.grid(row=0, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La imagen resultante al cifrar se guardar?? en el proyecto como "
                                            "imagenCifrada.jpg",bg="black",fg='white')
        labelCifrar.grid(row=1, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La imagen resultante al descifrar se guardar?? en el proyecto como"
                                            " imagen.jpg",bg="black",fg='white')
        labelCifrar.grid(row=2, column=0,sticky=W)

        self.image1=""
        imageLabelFrame= LabelFrame(self)
        imageLabelFrame.place(x=80, y=160)
        imageLabelFrame.configure(width=400, height=400)
        imageLabel=Label(imageLabelFrame, image=self.image1)
        imageLabel.place(x=200,y=200, anchor="center")

        self.image2=""
        imageLabelFrame2= LabelFrame(self)
        imageLabelFrame2.place(x=580, y=160)
        imageLabelFrame2.configure(width=400, height=400)
        imageLabel2=Label(imageLabelFrame2, image=self.image2)
        imageLabel2.place(x=200,y=200, anchor="center")


        botonesImagen = Label(self,bg="black")
        botonesImagen.place(x=200,y=620)

        for i in range(2):
            botonesImagen.columnconfigure((0,i), weight=1, pad=30)
        for i in range(2):
            botonesImagen.rowconfigure((0,i), weight=1, pad=10)

        textoUrl=Text(self)
        textoUrl.configure(width=77,height=2)
        textoUrl.place(x=200,y=580)

        def limpiar():
            imageLabel.configure(image="")
            imageLabel2.configure(image="")
            textoUrl.delete("1.0", END)
        
        def imagenUrl():
            url=textoUrl.get("1.0","end-1c")
            try:
                loadImage(url)
                self.image1=ImageTk.PhotoImage(file='imagen.jpg')
                imageLabel.configure(image=self.image1)
            except:
                messagebox.showinfo("Advertencia","No se ha proporcionado una Url correcta o no se puede acceder a ella.")
                main_window.deiconify()

        def imagenCargar():
            ruta=textoUrl.get("1.0","end-1c")
            loadImage3(ruta)
            try:
                imageLabel.configure(image="")
                self.image1=ImageTk.PhotoImage(file='imagen.jpg')
                imageLabel.configure(image=self.image1)
            except:
                messagebox.showinfo("Advertencia","No se puede acceder a la ruta especificada o el archivo no existe.")
                main_window.deiconify()                

        def cifrar():
            try:
                if not(imageLabel.cget("image")==""):
                    imageLabel2.configure(image="")
                    hillImagenCifrar()
                    self.image2=ImageTk.PhotoImage(file='imagenCifrada.jpg')
                    imageLabel2.configure(image=self.image2)
            except:
                messagebox.showinfo("Advertencia","Hay un error con la imagen.")
                main_window.deiconify()   
        
        def descifrar():
            try:
                if not(imageLabel.cget("image")==""):
                    imageLabel2.configure(image="")
                    hillImagenDescifrar()
                    self.image2=ImageTk.PhotoImage(file='imagen.jpg')
                    imageLabel2.configure(image=self.image2)
            except:
                messagebox.showinfo("Advertencia","Hay un error con la imagen o la clave no existe.")
                main_window.deiconify() 
        
        def cargarUltima():
            try:
                limpiar()
                self.image1=ImageTk.PhotoImage(file='imagenCifrada.jpg')
                imageLabel.configure(image=self.image1)
            except:
                messagebox.showinfo("Advertencia","No hay ninguna imagen cifrada.")
                main_window.deiconify()
            

        botonUrl =Button(botonesImagen, command=imagenUrl, text="Cargar imagen desde Url", padx=5, pady=5
                         ,font=('Comic Sans MS', 15, 'bold'))
        botonUrl.grid(row=1,column=0)

        botonCargar =Button(botonesImagen, command=imagenCargar, text="Cargar imagen desde la ruta espeficicada",
                            padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonCargar.grid(row=1,column=1)

        botonCifrar =Button(botonesImagen, command=cifrar, text="Cifrar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonCifrar.grid(row=2,column=0)

        botonDescifrar =Button(botonesImagen, command=descifrar, text="Descifrar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonDescifrar.grid(row=2,column=1)

        botonLimpiar =Button(botonesImagen, command=limpiar, text="Limpiar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonLimpiar.grid(row=2,column=2)

        botonCargarUltima =Button(botonesImagen, command=cargarUltima, text="Cargar ??ltima imagen cifrada", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'))
        botonCargarUltima.grid(row=1,column=2)



    def seleccion(self, event):
        index=0
        if (self.combo.get()=="Desplazamiento"):
                index=0
        elif (self.combo.get()=="Af??n"):
                index=1
        elif (self.combo.get()=="Vigenere"):
                index=2
        elif (self.combo.get()=="Sustituci??n"):
                index=3
        elif (self.combo.get()=="Hill"):
                index=4
        elif (self.combo.get()=="Permutaci??n"):
                index=5
        if (not self.combo.get()=="Hill para Imagen"):
            self = CriptoSistemas(mainWindow)
            self.combo.current(index)



class Criptoanalisis(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        global window
        window = main_window
        main_window.title("Criptoan??lisis")
        main_window.configure(width=780, height=800,bg="black")
        main_window.iconbitmap('moon.ico')
        main_window.resizable(0, 0)
        self.place(width=1400, height=950)
        self.style = ttk.Style()
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.style.theme_use('clam')
        self.imagespace = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrames = LabelFrame(self)
        imageLabelFrames.place(x=0, y=0)
        imageLabelFrames.configure(width=3000, height=3000)
        imageLabels = Label(imageLabelFrames, image=self.imagespace)
        imageLabels.place(x=200, y=200, anchor="center")

        self.combo = ttk.Combobox(self,state='readonly')
        self.combo.place(x=30, y=30)
        self.combo["values"] = ["Desplazamiento", "Af??n", "Vigenere", "Sustituci??n","Hill"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)

    def seleccion(self, event):
        if (self.combo.get()=="Desplazamiento"):
            self = Criptoanalisis(window)
            self.combo.current(0)
            analisis = LabelFrame(self, text="An??lisis", padx=5, pady=5,bg="black",fg="white")
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto cifrado",bg="black",fg="white")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=26,width=40, bg="light yellow", foreground="#000000")
            
            textoPlano=Label(analisis, text="Posibles Claves",bg="black",fg="white")
            textoPlano.grid(row=0,column=1, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=1,column=1, padx=4, pady=2)
            ptexto.configure(height=26,width=40, bg="light cyan", foreground="#000000", state="disabled")

            def analizar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                if (not text.isalpha()):
                    messagebox.showinfo("Advertencia", "S??lo se admiten letras en el texto.")
                    window.deiconify()
                else:
                    lista = desplazamientoAnalisis(text)
                    ptexto.configure(state='normal')
                    ptexto.delete("1.0", END)
                    for i in lista:
                        ptexto.insert(INSERT, i+"\n")
                    ptexto.configure(state='disabled')

            botonesFrame = Frame(analisis,bg="black")
            botonesFrame.grid(row=10,column=0, padx=5, pady=20)

            botonAnalisis =Button(botonesFrame, command=analizar, text="An??lisis", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
            botonAnalisis.grid(row=4,column=0)
        
        elif (self.combo.get()=="Af??n"):
            self = Criptoanalisis(window)
            self.combo.current(1)
            analisis = LabelFrame(self, text="An??lisis", padx=5, pady=5,bg="black",fg="white")
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto cifrado",bg="black",fg="white")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=26,width=40, bg="light yellow", foreground="#000000")
            
            textoPlano=Label(analisis, text="Posibles Claves",bg="black",fg="white")
            textoPlano.grid(row=0,column=1, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=1,column=1, padx=4, pady=2)
            ptexto.configure(height=26,width=40, bg="light cyan", foreground="#000000", state="disabled")

            def analizar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                if (not text.isalpha()):
                    messagebox.showinfo("Advertencia", "S??lo se admiten letras en el texto.")
                    window.deiconify()
                else:
                    lista = affineAnalisis(text)
                    ptexto.configure(state='normal')
                    ptexto.delete("1.0", END)
                    for i in lista:
                        ptexto.insert(INSERT, i+"\n")
                    ptexto.configure(state='disabled')

            botonesFrame = Frame(analisis,bg="black")
            botonesFrame.grid(row=10,column=0, padx=5, pady=20)

            botonAnalisis =Button(botonesFrame, command=analizar, text="An??lisis", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
            botonAnalisis.grid(row=4,column=0)

        elif (self.combo.get()=="Vigenere"):
            self = Criptoanalisis(window)
            self.combo.current(2)
            analisis = LabelFrame(self, text="An??lisis", padx=5, pady=5,bg="black",fg="white")
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto cifrado",bg="black",fg="white")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=26,width=40, bg="light yellow", foreground="#000000")
            
            textoPlano=Label(analisis, text="Posible descifrado",bg="black",fg="white")
            textoPlano.grid(row=0,column=1, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=1,column=1, padx=4, pady=2)
            ptexto.configure(height=26,width=40, bg="light cyan", foreground="#000000", state="disabled")

            def analizar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                if (not text.isalpha()):
                    messagebox.showinfo("Advertencia", "S??lo se admiten letras en el texto.")
                    window.deiconify()
                else:
                    password = vigenereClave(text)
                    ptexto.configure(state='normal')
                    ptexto.delete("1.0", END)
                    ptexto.insert(INSERT, vigenereDescifrar(text,password))
                    ptexto.configure(state='disabled')
                    textClave.configure(state='normal')
                    textClave.delete("1.0", END)
                    textClave.insert(INSERT, password.upper())
                    textClave.configure(state='disabled')

            botonesFrame = Frame(analisis,bg="black")
            botonesFrame.grid(row=2,column=0, padx=5, pady=20)

            labelPosibleClave = Label(botonesFrame, text="Posible Clave: ",bg="black",fg="white")
            labelPosibleClave.grid(row=0,column=1,padx=20,pady=5)

            textClave = Text(botonesFrame)
            textClave.grid(row=0,column=2, padx=4, pady=5)
            textClave.configure(height=1,width=10, foreground="#000000", background="#FFFFFF", state="disabled")

            botonAnalisis =Button(botonesFrame, command=analizar, text="An??lisis", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
            botonAnalisis.grid(row=0,column=0)

        elif (self.combo.get()=="Sustituci??n"):
            self = Criptoanalisis(window)
            window.configure(width=1400, height=950)
            self.place(width=1400, height=950)
            self.combo.current(3)         
            analisis = LabelFrame(self, text="An??lisis", padx=5, pady=5,bg="black",fg="white")
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto cifrado",bg="black",fg="white")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=19,width=40, bg="light yellow", foreground="#000000")

            botonesFrame = Frame(analisis,bg="black")
            botonesFrame.grid(row=2,column=0, padx=5, pady=20)

            labelPosibleClave = Label(botonesFrame, text="Posible Clave: ",bg="black",fg="white")
            labelPosibleClave.grid(row=1,column=0,padx=10,pady=5)

            textClave = Text(botonesFrame)
            textClave.grid(row=1,column=1, padx=4, pady=5)
            textClave.configure(height=1,width=26, foreground="#000000")
            textClave.insert(INSERT,"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            textClave.configure(state="disabled")

            def ingresarFrecuencias():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                listaMonogramas = frecuenciaMonogramas(text)
                listaMono2.delete(*listaMono2.get_children())
                for i in range(len(listaMonogramas)):
                    listaMono2.insert("",END,text=listaMonogramas[i][0], values=(listaMonogramas[i][1]))

                listaDigramas = frecuenciaDigramas(text)
                listaDupla2.delete(*listaDupla2.get_children())
                for i in range(len(listaDigramas)):
                    listaDupla2.insert("",END,text=listaDigramas[i][0], values=(listaDigramas[i][1]))

                listaTrigramas = frecuenciaTrigramas(text)
                listaTripla2.delete(*listaTripla2.get_children())
                for i in range(len(listaTrigramas)):
                    listaTripla2.insert("",END,text=listaTrigramas[i][0], values=(listaTrigramas[i][1]))

                
            botonAnalisis =Button(botonesFrame, command=ingresarFrecuencias, text="An??lisis", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
            botonAnalisis.grid(row=0,column=0)

            def descifrar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")

                passSuma=""
                passSuma=passSuma+comboA.get()+comboB.get()+comboC.get()+comboD.get()+comboE.get()+comboF.get()+comboG.get()+comboH.get()+comboI.get()+comboJ.get()
                passSuma=passSuma+comboK.get()+comboL.get()+comboM.get()+comboN.get()+comboO.get()+comboP.get()+comboQ.get()+comboR.get()+comboS.get()+comboT.get()
                passSuma=passSuma+comboU.get()+comboV.get()+comboW.get()+comboX.get()+comboY.get()+comboZ.get()

                textClave.configure(state="normal")
                textClave.delete("1.0", END)
                textClave.insert(INSERT,passSuma)
                textClave.configure(state="disabled")


                password=textClave.get("1.0","end-1c")
                boolPass=True
                if (not text.isalpha()) and not text.split(" ")==['']:
                        messagebox.showinfo("Advertencia", "S??lo se admiten letras en el texto.")
                        window.deiconify()
                for i in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                    if i not in list(password):
                        boolPass=False
                if (not boolPass):
                        messagebox.showinfo("Advertencia","Debe generar una clave que contenga todas las letras.")
                        window.deiconify()
                else:
                    ptexto.configure(state='normal')
                    ptexto.delete("1.0", END)
                    ptexto.insert(INSERT, sustitucionDescifrar(text,password))
                    ptexto.configure(state='disabled')               

            botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
            botonDescifrar.grid(row=0,column=1)
            
            textoPlano=Label(analisis, text="Posible descifrado",bg="black",fg="white")
            textoPlano.grid(row=3,column=0, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=4,column=0, padx=4, pady=2)
            ptexto.configure(height=19,width=40, bg="light cyan", foreground="#000000", state="disabled")


            letrasCombo = LabelFrame(self, text="Cambiar letras", padx=5, pady=5)
            letrasCombo.place(x=380, y=60)

            textoA=Label(letrasCombo, text="A: ")
            textoA.grid(row=0,column=0, padx=5, pady=5, sticky=W)

            comboA = ttk.Combobox(letrasCombo,state='readonly')
            comboA.grid(row=0, column=1)
            comboA["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboA.current(0)

            textoB=Label(letrasCombo, text="B: ")
            textoB.grid(row=1,column=0, padx=5, pady=5, sticky=W)

            comboB = ttk.Combobox(letrasCombo,state='readonly')
            comboB.grid(row=1, column=1)
            comboB["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboB.current(1)

            textoC=Label(letrasCombo, text="C: ")
            textoC.grid(row=2,column=0, padx=5, pady=5, sticky=W)

            comboC = ttk.Combobox(letrasCombo,state='readonly')
            comboC.grid(row=2, column=1)
            comboC["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboC.current(2)
            
            textoD=Label(letrasCombo, text="D: ")
            textoD.grid(row=3,column=0, padx=5, pady=5, sticky=W)

            comboD = ttk.Combobox(letrasCombo,state='readonly')
            comboD.grid(row=3, column=1)
            comboD["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboD.current(3)

            textoE=Label(letrasCombo, text="E: ")
            textoE.grid(row=4,column=0, padx=5, pady=5, sticky=W)

            comboE = ttk.Combobox(letrasCombo,state='readonly')
            comboE.grid(row=4, column=1)
            comboE["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboE.current(4)

            textoF=Label(letrasCombo, text="F: ")
            textoF.grid(row=5,column=0, padx=5, pady=5, sticky=W)

            comboF = ttk.Combobox(letrasCombo,state='readonly')
            comboF.grid(row=5, column=1)
            comboF["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboF.current(5)

            textoG=Label(letrasCombo, text="G: ")
            textoG.grid(row=6,column=0, padx=5, pady=5, sticky=W)

            comboG = ttk.Combobox(letrasCombo,state='readonly')
            comboG.grid(row=6, column=1)
            comboG["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboG.current(6)

            textoH=Label(letrasCombo, text="H: ")
            textoH.grid(row=7,column=0, padx=5, pady=5, sticky=W)

            comboH = ttk.Combobox(letrasCombo,state='readonly')
            comboH.grid(row=7, column=1)
            comboH["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboH.current(7)

            textoI=Label(letrasCombo, text="I: ")
            textoI.grid(row=8,column=0, padx=5, pady=5, sticky=W)

            comboI = ttk.Combobox(letrasCombo,state='readonly')
            comboI.grid(row=8, column=1)
            comboI["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboI.current(8)

            textoJ=Label(letrasCombo, text="J: ")
            textoJ.grid(row=9,column=0, padx=5, pady=5, sticky=W)

            comboJ = ttk.Combobox(letrasCombo,state='readonly')
            comboJ.grid(row=9, column=1)
            comboJ["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboJ.current(9)

            textoK=Label(letrasCombo, text="K: ")
            textoK.grid(row=10,column=0, padx=5, pady=5, sticky=W)

            comboK = ttk.Combobox(letrasCombo,state='readonly')
            comboK.grid(row=10, column=1)
            comboK["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboK.current(10)

            textoL=Label(letrasCombo, text="L: ")
            textoL.grid(row=11,column=0, padx=5, pady=5, sticky=W)

            comboL = ttk.Combobox(letrasCombo,state='readonly')
            comboL.grid(row=11, column=1)
            comboL["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboL.current(11)

            textoM=Label(letrasCombo, text="M: ")
            textoM.grid(row=12,column=0, padx=5, pady=5, sticky=W)

            comboM = ttk.Combobox(letrasCombo,state='readonly')
            comboM.grid(row=12, column=1)
            comboM["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboM.current(12)

            textoN=Label(letrasCombo, text="N: ")
            textoN.grid(row=13,column=0, padx=5, pady=5, sticky=W)

            comboN = ttk.Combobox(letrasCombo,state='readonly')
            comboN.grid(row=13, column=1)
            comboN["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboN.current(13)

            textoO=Label(letrasCombo, text="O: ")
            textoO.grid(row=14,column=0, padx=5, pady=5, sticky=W)

            comboO = ttk.Combobox(letrasCombo,state='readonly')
            comboO.grid(row=14, column=1)
            comboO["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboO.current(14)

            textoP=Label(letrasCombo, text="P: ")
            textoP.grid(row=15,column=0, padx=5, pady=5, sticky=W)

            comboP = ttk.Combobox(letrasCombo,state='readonly')
            comboP.grid(row=15, column=1)
            comboP["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboP.current(15)

            textoQ=Label(letrasCombo, text="Q: ")
            textoQ.grid(row=16,column=0, padx=5, pady=5, sticky=W)

            comboQ = ttk.Combobox(letrasCombo,state='readonly')
            comboQ.grid(row=16, column=1)
            comboQ["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboQ.current(16)

            textoR=Label(letrasCombo, text="R: ")
            textoR.grid(row=17,column=0, padx=5, pady=5, sticky=W)

            comboR = ttk.Combobox(letrasCombo,state='readonly')
            comboR.grid(row=17, column=1)
            comboR["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboR.current(17)

            textoS=Label(letrasCombo, text="S: ")
            textoS.grid(row=18,column=0, padx=5, pady=5, sticky=W)

            comboS = ttk.Combobox(letrasCombo,state='readonly')
            comboS.grid(row=18, column=1)
            comboS["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboS.current(18)

            textoT=Label(letrasCombo, text="T: ")
            textoT.grid(row=19,column=0, padx=5, pady=5, sticky=W)

            comboT = ttk.Combobox(letrasCombo,state='readonly')
            comboT.grid(row=19, column=1)
            comboT["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboT.current(19)

            textoU=Label(letrasCombo, text="U: ")
            textoU.grid(row=20,column=0, padx=5, pady=5, sticky=W)

            comboU = ttk.Combobox(letrasCombo,state='readonly')
            comboU.grid(row=20, column=1)
            comboU["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboU.current(20)

            textoV=Label(letrasCombo, text="V: ")
            textoV.grid(row=21,column=0, padx=5, pady=5, sticky=W)

            comboV = ttk.Combobox(letrasCombo,state='readonly')
            comboV.grid(row=21, column=1)
            comboV["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboV.current(21)

            textoW=Label(letrasCombo, text="W: ")
            textoW.grid(row=22,column=0, padx=5, pady=5, sticky=W)

            comboW = ttk.Combobox(letrasCombo,state='readonly')
            comboW.grid(row=22, column=1)
            comboW["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboW.current(22)

            textoX=Label(letrasCombo, text="X: ")
            textoX.grid(row=23,column=0, padx=5, pady=5, sticky=W)

            comboX = ttk.Combobox(letrasCombo,state='readonly')
            comboX.grid(row=23, column=1)
            comboX["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboX.current(23)

            textoY=Label(letrasCombo, text="Y: ")
            textoY.grid(row=24,column=0, padx=5, pady=5, sticky=W)

            comboY = ttk.Combobox(letrasCombo,state='readonly')
            comboY.grid(row=24, column=1)
            comboY["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboY.current(24)

            textoZ=Label(letrasCombo, text="Z: ")
            textoZ.grid(row=25,column=0, padx=5, pady=5, sticky=W)

            comboZ = ttk.Combobox(letrasCombo,state='readonly')
            comboZ.grid(row=25, column=1)
            comboZ["values"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            comboZ.current(25)

            botonAnalisis =Button(self, command="", text="An??lisis", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
            botonAnalisis.place(x=500,y=1000)

            listaMono = ttk.Treeview(self, columns=("Probabilidad"), height=26)
            listaMono.column("#0", width=80)
            listaMono.heading("#0", text="Caracter")
            listaMono.column("Probabilidad", width=80)
            listaMono.heading("Probabilidad", text="Frecuencia")
            listaMono.place(x=620, y=60)
            frec=[0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
            letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            listaDuplas=list()
            for i in range(26):
                listaDuplas.append([letras[i],frec[i]])
            listaDuplas.sort(key = lambda x: x[1])
            for i in range(26):
                listaMono.insert("",END,text=listaDuplas[25-i][0], values=(listaDuplas[25-i][1]))

            listaMono2 = ttk.Treeview(self, columns=("Recurrencia"), height=26)
            listaMono2.column("#0", width=80)
            listaMono2.heading("#0", text="Monograma")
            listaMono2.column("Recurrencia", width=80)
            listaMono2.heading("Recurrencia", text="Repeticiones")
            listaMono2.place(x=800, y=60)

            listaDupla = ttk.Treeview(self, columns=("Probabilidad"), height=16)
            listaDupla.column("#0", width=80)
            listaDupla.heading("#0", text="Digrama")
            listaDupla.column("Probabilidad", width=80)
            listaDupla.heading("Probabilidad", text="Frecuencia")
            listaDupla.place(x=1000, y=60)
            digramas = [('he',0.0128), ('th', 0.0152), ('in', 0.0094), ('er', 0.0094), ('an', 0.0084), ('re', 0.0064), ('nd', 0.0063),
                ('at', 0.0059), ('on', 0.0057), ('nt', 0.0056), ('ha', 0.0056), ('es', 0.0056), ('st', 0.0055), ('en', 0.0055),
                ('ed', 0.0053), ('to', 0.0052)]
            digramas.sort(key = lambda x: x[1])
            for i in range(16):
                listaDupla.insert("",END,text=digramas[15-i][0].upper(), values=(digramas[15-i][1]))
            listaDupla2 = ttk.Treeview(self, columns=("Recurrencia"), height=16)
            listaDupla2.column("#0", width=80)
            listaDupla2.heading("#0", text="Digrama")
            listaDupla2.column("Recurrencia", width=80)
            listaDupla2.heading("Recurrencia", text="Repeticiones")
            listaDupla2.place(x=1200, y=60)
            
            listaTripla = ttk.Treeview(self, columns=("Probabilidad"), height=8)
            listaTripla.column("#0", width=80)
            listaTripla.heading("#0", text="Trigrama")
            listaTripla.column("Probabilidad", width=80)
            listaTripla.heading("Probabilidad", text="Frecuencia")
            listaTripla.place(x=620, y=630)
            trigramas = [('the', 0.0181), ('and', 0.0073), ('tha', 0.0033), ('ent', 0.0042), ('ing', 0.007), ('ion', 0.0042), ('tio', 0.0031),
                 ('for', 0.0034)]
            trigramas.sort(key = lambda x: x[1])
            for i in range(8):
                listaTripla.insert("",END,text=trigramas[7-i][0].upper(), values=(digramas[7-i][1]))
            #this coomment is not funny
            listaTripla2 = ttk.Treeview(self, columns=("Recurrencia"), height=8)
            listaTripla2.column("#0", width=80)
            listaTripla2.heading("#0", text="Trigrama")
            listaTripla2.column("Recurrencia", width=80)
            listaTripla2.heading("Recurrencia", text="Repeticiones")
            listaTripla2.place(x=800, y=630)

        elif (self.combo.get()=="Hill"):
            self = Criptoanalisis(window)
            self.combo.current(4)
            analisis = LabelFrame(self, text="An??lisis", padx=5, pady=5,bg="black",fg="white")
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto plano",bg="black",fg="white")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=26,width=40, bg="light yellow", foreground="#000000")
            
            textoPlano=Label(analisis, text="Texto cifrado",bg="black",fg="white")
            textoPlano.grid(row=0,column=1, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=1,column=1, padx=4, pady=2)
            ptexto.configure(height=26,width=40, bg="light cyan", foreground="#000000")

            def analizar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                text2=ptexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                if (not text.isalpha()):
                    messagebox.showinfo("Advertencia", "S??lo se admiten letras en ambos textos.")
                    window.deiconify()
                elif (not text2.isalpha()):
                    messagebox.showinfo("Advertencia", "S??lo se admiten letras en ambos texto.")
                    window.deiconify()
                
                else:   
                    textClave.configure(state='normal')
                    textClave.delete("1.0", END)
                    textClave.configure(state='disabled')
                    try:
                        claves = CriptoanalisisHill(text,text2)
                        if(claves==[]):
                            messagebox.showinfo("Advertencia", "A partir de los textos no se puede encontrar una clave.")
                            window.deiconify()
                        for i in claves:
                            textClave.configure(state='normal')
                            textClave.insert(INSERT, "Una posible clave es "+ i[0] + " que corresponde a una matriz de dimensi??n m = "+str(i[1])+".\n")
                            textClave.configure(state='disabled')
                    except:
                        messagebox.showinfo("Advertencia", "A partir de los textos no se puede encontrar una clave.")
                        window.deiconify()
                        


            botonesFrame = Frame(analisis,bg="black")
            botonesFrame.grid(row=2,column=0, padx=5, pady=20)

            labelPosibleClave = Label(analisis, text="Posibles Claves: ",bg="black",fg="white")
            labelPosibleClave.grid(row=3,column=0,padx=20,pady=5, sticky=W)

            labelEspacio = Label(analisis, text="",bg="black",fg="white")
            labelEspacio.grid(row=4,column=0,padx=20,pady=5, sticky=W)
            labelEspacio.configure(width=1,height=10)


            textClave = Text(self)
            textClave.place(x=40,y=650)
            textClave.configure(height=6,width=81, foreground="#000000", background="#FFFFFF", state="disabled")

            botonAnalisis =Button(botonesFrame, command=analizar, text="An??lisis", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
            botonAnalisis.grid(row=0,column=0)



class CriptoBloque(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        global mainWindow
        mainWindow=main_window
        main_window.title("Criptosistemas en Bloque")
        main_window.configure(width=1200, height=750,bg="black")
        main_window.iconbitmap('moon.ico')
        main_window.resizable(0, 0)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1200, height=1200)
        self.imagespace = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrames = LabelFrame(self)
        imageLabelFrames.place(x=0, y=0)
        imageLabelFrames.configure(width=3000, height=3000)
        imageLabels = Label(imageLabelFrames, image=self.imagespace)
        imageLabels.place(x=200, y=200, anchor="center")

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5,bg="black",fg="white")
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5,bg="black",fg="white")
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["DES", "3-DES", "AES", "S-DES"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)
        self.combo.current(0)

        modoLabel = Label(opcionesCifrado, text="Modo: ", padx=5, pady=5,bg="black",fg="white")
        modoLabel.grid(row=1, column=0)

        self.modo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.modo.grid(row=1, column=1)
        self.modo["values"] = ["ECB", "CBC", "CFB", "OFB"]
        self.modo.bind("<<ComboboxSelected>>", self.seleccion)
        self.modo.current(0)

        claveLabel = Label(opcionesCifrado, text="Clave: ", padx=5, pady=5,bg="black",fg="white")
        claveLabel.grid(row=2, column=0)

        clave=Text(opcionesCifrado)
        clave.grid(row=2,column=1, sticky=W)
        clave.configure(height=1,width=16, padx=5, pady=5)


        def selection():
            choice = var.get()
            if choice == 1:
                m = 16
            elif choice == 2:
                m = 24
            elif choice == 3:
                m = 32
            return m

        global labelSize
        labelSize=LabelFrame(self)
        labelSize.place(x=250,y=67)
        var =IntVar()
        Radiobutton(labelSize, text='16 bytes', variable=var, value=1,command=selection).pack()
        Radiobutton(labelSize, text='24 bytes', variable=var, value=2,command=selection).pack(anchor=W)
        Radiobutton(labelSize, text='32 bytes', variable=var, value=3,command=selection).pack()

        labelSize.place_forget()

        labelInfo=LabelFrame(self,text="Informaci??n",bg="black",fg="white")
        labelInfo.place(x=330,y=30)
        labelClave = Label(labelInfo, text="Al cifrar sin proporcionar clave, esta se generar?? autom??ticamente. "
                                           "El vector inicial siempre se genera autom??ticamente."
                           ,bg='black',fg='white')
        labelClave.grid(row=0, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La clave y vector inicial usados para CIFRAR se guardar??n "
                                            "en el archivo key.txt y ivk.txt respectivamente en la carpeta "
                                            "del proyecto.",bg='black',fg='white')
        labelCifrar.grid(row=3, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="Si no se proporciona clave para descifrar, se usar?? la guardada en"
                                            " el archivo key.txt (si hay). El vector inicial ser?? el almacenado "
                                            "en ivk.txt",bg='black',fg='white')
        labelCifrar.grid(row=4, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La imagen resultante al cifrar se guardar?? en el proyecto como"
                                            " imagenCifrada.bmp",bg='black',fg='white')
        labelCifrar.grid(row=1, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La imagen resultante al descifrar se guardar?? en el proyecto "
                                            "como imagen.bmp",bg='black',fg='white')
        labelCifrar.grid(row=2, column=0,sticky=W)
        

        self.image1=""
        imageLabelFrame= LabelFrame(self)
        imageLabelFrame.place(x=80, y=160)
        imageLabelFrame.configure(width=400, height=400)
        imageLabel=Label(imageLabelFrame, image=self.image1)
        imageLabel.place(x=200,y=200, anchor="center")

        self.image2=""
        imageLabelFrame2= LabelFrame(self)
        imageLabelFrame2.place(x=580, y=160)
        imageLabelFrame2.configure(width=400, height=400)
        imageLabel2=Label(imageLabelFrame2, image=self.image2)
        imageLabel2.place(x=200,y=200, anchor="center")

        botonesImagen = Frame(self, bg='black',bd='1')
        botonesImagen.place(x=100,y=620)

        for i in range(2):
            botonesImagen.columnconfigure((0,i), weight=1, pad=30)
        for i in range(2):
            botonesImagen.rowconfigure((0,i), weight=1, pad=10)

        textoUrl=Text(self)
        textoUrl.configure(width=77,height=2)
        textoUrl.place(x=200,y=580)

        def limpiar():
            imageLabel.configure(image="")
            imageLabel2.configure(image="")
            textoUrl.delete("1.0", END)
        
        def imagenUrl():
            url=textoUrl.get("1.0","end-1c")
            try:
                loadImageBlock(url)
                self.image1=ImageTk.PhotoImage(file='imagen.bmp')
                imageLabel.configure(image=self.image1)
            except:
                messagebox.showinfo("Advertencia","No se ha proporcionado una Url correcta o no se puede acceder a ella.")
                main_window.deiconify()

        def imagenCargar():
            ruta=textoUrl.get("1.0","end-1c")
            loadImage3Block(ruta)
            try:
                imageLabel.configure(image="")
                self.image1=ImageTk.PhotoImage(file='imagen.bmp')
                imageLabel.configure(image=self.image1)
            except:
                messagebox.showinfo("Advertencia","No se puede acceder a la ruta especificada o el archivo no existe.")
                main_window.deiconify()                

        def cifrar():
            try:
                if not(imageLabel.cget("image")==""):
                    imageLabel2.configure(image="")
                    key=clave.get("1.0","end-1c")
                    if(len(key)<1):
                        key=""
                    if (self.combo.get())=='DES':
                        DesCifrar(self.modo.get(),key)
                    elif (self.combo.get())=='3-DES':
                        Des3Cifrar(self.modo.get(),key)
                    elif (self.combo.get())=='AES':
                        bt=selection()
                        AesCifrar(self.modo.get(),key,bt)
                    self.image2=ImageTk.PhotoImage(file='imagenCifrada.bmp')
                    imageLabel2.configure(image=self.image2)
            except:
                messagebox.showinfo("Advertencia","Hay un error con la imagen o la clave.")
                main_window.deiconify()
        
        def descifrar():
            try:
                if not(imageLabel.cget("image")==""):
                    imageLabel2.configure(image="")
                    key=clave.get("1.0","end-1c")
                    if(len(key)<1):
                        key=""
                    if (self.combo.get())=='DES':
                        DesDescifrar(self.modo.get(),key)
                    elif (self.combo.get())=='3-DES':
                        Des3Descifrar(self.modo.get(),key)
                    elif (self.combo.get())=='AES':
                        bt=selection()
                        AesDescifrar(self.modo.get(),key,bt)
                    self.image2=ImageTk.PhotoImage(file='imagen.bmp')
                    imageLabel2.configure(image=self.image2)
            except:
                messagebox.showinfo("Advertencia","Hay un error con la imagen o la clave.")
                main_window.deiconify() 
        
        def cargarUltima():
            try:
                limpiar()
                self.image1=ImageTk.PhotoImage(file='imagenCifrada.bmp')
                imageLabel.configure(image=self.image1)
            except:
                messagebox.showinfo("Advertencia","No hay ninguna imagen cifrada.")
                main_window.deiconify()
            

        botonUrl =Button(botonesImagen, command=imagenUrl, text="Cargar imagen desde Url", padx=5, pady=5,
                         font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonUrl.grid(row=1,column=0)

        botonCargar =Button(botonesImagen, command=imagenCargar, text="Cargar imagen desde la ruta espeficicada",
                            padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonCargar.grid(row=1,column=1)

        botonCifrar =Button(botonesImagen, command=cifrar, text="Cifrar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonCifrar.grid(row=2,column=0)

        botonDescifrar =Button(botonesImagen, command=descifrar, text="Descifrar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonDescifrar.grid(row=2,column=1)

        botonLimpiar =Button(botonesImagen, command=limpiar, text="Limpiar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonLimpiar.grid(row=2,column=2)

        botonCargarUltima =Button(botonesImagen, command=cargarUltima, text="Cargar ??ltima imagen cifrada", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')

        botonCargarUltima.grid(row=1,column=2)

    def seleccion(self, event):
        if (self.combo.get()=="DES"):
                index=0
                labelSize.place_forget()
        elif (self.combo.get()=="3-DES"):
                index=1
                labelSize.place_forget()
        elif (self.combo.get()=="AES"):
                index=2
                labelSize.place(x=250, y=67)
        elif (self.combo.get()=="S-DES"):
            self = CriptoBloqueTexto(mainWindow)
            self.combo.current(3)



class CriptoBloqueTexto(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Criptosistemas en Bloque")
        main_window.configure(width=1300, height=500,bg="black")
        main_window.iconbitmap('moon.ico')
        main_window.resizable(0, 0)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1300, height=500)

        self.imagespace = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrames = LabelFrame(self)
        imageLabelFrames.place(x=0, y=0)
        imageLabelFrames.configure(width=3000, height=3000)
        imageLabels = Label(imageLabelFrames, image=self.imagespace)
        imageLabels.place(x=200, y=200, anchor="center")


        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5,bg="black",fg="white")
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5,bg="black",fg="white")
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["DES", "3-DES", "AES", "S-DES"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)

        modoLabel = Label(opcionesCifrado, text="Modo: ", padx=5, pady=5,bg="black",fg="white")
        modoLabel.grid(row=1, column=0)

        self.modo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.modo.grid(row=1, column=1)
        self.modo["values"] = ["ECB", "CBC", "CFB", "OFB"]
        self.modo.bind("<<ComboboxSelected>>", self.seleccion)
        self.modo.current(0)

        claveLabel = Label(opcionesCifrado, text="Clave: ", padx=5, pady=5,bg="black",fg="white")
        claveLabel.grid(row=2, column=0)

        clave=Text(opcionesCifrado)
        clave.grid(row=2,column=1, sticky=W)
        clave.configure(height=1,width=16, padx=5, pady=5)

        cifrarFrame = LabelFrame(self, text="Cifrar",bg="black",fg="white")
        cifrarFrame.place(x=30, y=180)

        ctClaro = Label(cifrarFrame, text="Texto",bg="black",fg="white")
        ctClaro.grid(row=0, sticky=W)

        ctCifrado = Label(cifrarFrame, text="Resultado",bg="black",fg="white")
        ctCifrado.grid(row=0, column=1, sticky=W, padx=4, pady=2)

        texto=Text(cifrarFrame)
        texto.grid(row=1,column=0, padx=4, pady=2)
        texto.configure(height=10,width=25, bg="light yellow", foreground="#000000")

        resultado=Text(cifrarFrame)
        resultado.grid(row=1,column=1, padx=4, pady=2)
        resultado.configure(height=10,width=25, bg="light cyan", foreground="#000000", state="disabled")


        #funciones para los botones
        def cifrar():
            text=texto.get("1.0","end-1c")
            password=clave.get("1.0","end-1c").replace(" ","")
            try: 
                resultado.configure(state='normal')
                resultado.delete("1.0", END)
                resultado.insert(INSERT, SdesCifrar(text,password,self.modo.get()))
                resultado.configure(state='disabled')
            except:           
                messagebox.showinfo("Advertencia","Hay un error con el texto o la clave.")
                main_window.deiconify()
                
                           
        def descifrar():
            text=texto.get("1.0","end-1c").split(" ")
            password=clave.get("1.0","end-1c")
            try:    
                resultado.configure(state='normal')
                resultado.delete("1.0", END)
                resultado.insert(INSERT, SdesDescifrar(text,password,self.modo.get()))
                resultado.configure(state='disabled')
            except:
                if(self.modo.get()!='ECB'):
                    messagebox.showinfo("Advertencia","Hay un error con el texto, la clave o el vector inicial. Aseg??rese de que el valor del vector inicial est?? guardado en el archivo ivk.txt")
                else:
                    messagebox.showinfo("Advertencia","Hay un error con el texto o la clave.")
                main_window.deiconify()

        def copiar_al_portapapeles():
            self.clipboard_clear()
            self.clipboard_append(resultado.get("1.0","end-1c"))

        def pegar():
            texto.delete("1.0", END)
            texto.insert(INSERT, self.clipboard_get())
            
        def generarclave():
            if ((self.combo.get()) == 'S-DES'):
                clave.delete("1.0", END)
                clave.insert(1.0,"1001001101")

        def limpiar():
            resultado.configure(state='normal')
            resultado.delete("1.0", END)
            resultado.configure(state='disabled')
            texto.delete("1.0", END)

        botonesFrame = Frame(cifrarFrame, border=0,padx=5,pady=5,bg="black")
        botonesFrame.grid(row=2, column=0)

        botonesFrame2 = Frame(cifrarFrame, border=0,padx=5,pady=5,bg="black")
        botonesFrame2.grid(row=2, column=1)
        
        #espaciado entre botones
        for i in range(2):
            botonesFrame2.columnconfigure((0,i), weight=1, pad=30)
        for i in range(3):
            botonesFrame.columnconfigure((0,i), weight=1, pad=25)

        botonCifrar =Button(botonesFrame, command=cifrar, text="Cifrar", padx=5, pady=5
                            ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonCifrar.grid(row=0,column=0)

        botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5
                               ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonDescifrar.grid(row=0,column=1)  

        botonPegar =Button(botonesFrame, command=pegar, text="Pegar", padx=5, pady=5
                           ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonPegar.grid(row=0,column=2)       

        botonLimpiar =Button(botonesFrame2, command=limpiar, text="Limpiar", padx=5, pady=5
                             ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonLimpiar.grid(row=0,column=0)

        botonCopiar =Button(botonesFrame2, command=copiar_al_portapapeles, text="Copiar", padx=5, pady=5
                            ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonCopiar.grid(row=0,column=1)
        
        botonGenerarClave=Button(botonesFrame2, command=generarclave, text="Generar Clave", padx=5, pady=5
                                 ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonGenerarClave.grid(row=0,column=3)

        instrucciones = LabelFrame(self, text="Anotaciones ",bg="black",fg="white")
        instrucciones.place(x=500, y= 30)

        instruc1=Label(instrucciones, text="1. Si va a proporcionar una clave, debe corresponder a una cadena de"
                                           " 10 d??gitos formados por 0's y 1's.",bg="black",fg='white')
        instruc1.grid(row=0, column=0, stick=W)
        instruc1=Label(instrucciones, text="2. Si no se proporciona una clave, se generar?? autom??ticamente.",bg="black",fg='white')
        instruc1.grid(row=1, column=0, stick=W)
        instruc1=Label(instrucciones, text="3. La clave usada en el cifrado se guardar?? en el archivo key.txt.",bg="black",fg='white')
        instruc1.grid(row=2, column=0, stick=W)
        instruc1=Label(instrucciones, text="4. En los modos CBC, CBF y OFB el vector inicial se generar?? autom??ticamente y"
                                           " se guardar?? en el archivo ivk.txt",bg="black",fg='white')
        instruc1.grid(row=3, column=0, stick=W)
        instruc1=Label(instrucciones, text="5. Al momento de desencriptar en los modos CBC, CBF y OFB el vector "
                                           "inicial debe estar en el archivo ivk.txt",bg="black",fg='white')
        instruc1.grid(row=4, column=0, stick=W)

    def seleccion(self, event):
        index=0
        if (self.combo.get()=="DES"):
                index=0
        elif (self.combo.get()=="3-DES"):
                index=1
        elif (self.combo.get()=="AES"):
                index=2
        if (not self.combo.get()=="S-DES"):
            self = CriptoBloque(mainWindow)
            self.combo.current(index)
            if (self.combo.get()=="AES"):
                labelSize.place(x=250, y=67)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
class CriptoGamma(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Gamma Pentagonal")
        main_window.configure(width=1300, height=750,bg="black")
        main_window.iconbitmap('moon.ico')
        main_window.resizable(0, 0)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=3000, height=3000)
        self.imagespace = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrames = LabelFrame(self)
        imageLabelFrames.place(x=0, y=0)
        imageLabelFrames.configure(width=3000, height=3000)
        imageLabels = Label(imageLabelFrames, image=self.imagespace)
        imageLabels.place(x=200, y=200, anchor="center")

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5,bg="black",fg="white")
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Grafo: ", padx=5, pady=5,bg="black",fg="white")
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Grafo 1", "Grafo 2"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)
        self.combo.current(0)

        claveLabel = Label(opcionesCifrado, text="Permutaci??n: ", padx=5, pady=5,bg="black",fg="white")
        claveLabel.grid(row=1, column=0)

        clave=Text(opcionesCifrado)
        clave.grid(row=1,column=1, sticky=W)
        clave.configure(height=2,width=16, padx=5, pady=5)

        def aplicarPermut():
            try:
                permut=clave.get("1.0","end-1c").replace(" ","").replace("\n","").split('-')
                axs.clear()
                iniciarAlph()
                cargarPermut(permut)
                annotatePlot()
                canvas.draw()
            except:
                messagebox.showinfo("Advertencia","Hay un error con la permutaci??n proporcionada.")
                main_window.deiconify()

        botonAplicar =Button(opcionesCifrado, command=aplicarPermut, text="Aplicar", padx=5,
                             pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonAplicar.grid(row=2,column=0)

        def reiniciar():
            clave.delete("1.0", END)
            xText.delete("1.0", END)
            xText.insert(1.0, '0')
            yText.delete("1.0", END)
            yText.insert(1.0, '0')
            limpiar()
            permuta=genPermut()
            inicMatrix()
            axs.clear()
            iniciarAlph()
            cargarPermut(permuta)
            annotatePlot()
            canvas.draw()
            a.clear()
            self.combo.current(0)
            crearGrafo(0,0,0)
            canvas2.draw()

        botonReiniciar =Button(opcionesCifrado, command=reiniciar, text="Reiniciar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonReiniciar.grid(row=2,column=1)


        inicialFrame = LabelFrame(self, text="Coordenada inicial", padx=12, pady=5,bg="black",fg="white")
        inicialFrame.place(x=30,y=200)
        xLabel = Label(inicialFrame, text="X:", padx=5, pady=5)
        xLabel.grid(row=0, column =0)

        xText=Text(inicialFrame)
        xText.grid(row=0,column=1, sticky=W)
        xText.configure(height=1,width=3, padx=5, pady=5)
        xText.insert(1.0, '0')

        yLabel = Label(inicialFrame, text="Y:", padx=5, pady=5)
        yLabel.grid(row=0, column =2)

        yText=Text(inicialFrame)
        yText.grid(row=0,column=3, sticky=W)
        yText.configure(height=1,width=3, padx=5, pady=5)
        yText.insert(1.0, '0')

        def generarGrafo():
            try:
                axs.clear()
                xVal=xText.get("1.0","end-1c")
                yVal=yText.get("1.0","end-1c")
                aumentarAlph(int(xVal),int(yVal))
                iniciarAlph()
                annotatePlot()
                canvas.draw()
                modo=0
                if(self.combo.get()=="Grafo 2"):
                    modo=1
                a.clear()
                crearGrafo(int(xVal),int(yVal),modo)
                canvas2.draw()
            except:
                messagebox.showinfo("Advertencia", "Hay un error con las coordenadas.")
                main_window.deiconify()

        botonGenerar =Button(inicialFrame, command=generarGrafo, text="Generar grafo", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1'
                             )
        botonGenerar.grid(row=0,column=4)

        cifrarFrame = LabelFrame(self, text="Cifrar",bg="black",fg="white")
        cifrarFrame.place(x=400, y=30)

        ctClaro = Label(cifrarFrame, text="Texto",bg="black",fg="white")
        ctClaro.grid(row=0, sticky=W)

        ctCifrado = Label(cifrarFrame, text="Resultado",bg="black",fg="white")
        ctCifrado.grid(row=0, column=1, sticky=W, padx=4, pady=2)

        texto=Text(cifrarFrame)
        texto.grid(row=1,column=0, padx=4, pady=2)
        texto.configure(height=10,width=25, bg="light yellow", foreground="#000000")

        resultado=Text(cifrarFrame)
        resultado.grid(row=1,column=1, padx=4, pady=2)
        resultado.configure(height=10,width=25, bg="light cyan", foreground="#000000", state="disabled")

        permut=list()
        def genPermut():
            permuta = list()
            for i in range(10):
                permuta.append(str(i))
            return permuta
        permut=genPermut()
        
        matrixAlph = list()       
        def inicMatrix():
            del matrixAlph[:]
            for i in range(10):
                aux = list()
                for j in range(20):
                    aux.append(j)
                matrixAlph.append(aux)
        inicMatrix()

        fig, axs = plt.subplots(dpi=100, figsize=(5, 5), sharey=False, facecolor='#FFFFFF')
        fig.suptitle('Alfabeto')
        axs.grid(which="both", color="grey", linewidth=1, linestyle="-", alpha=0.2)

        def iniciarAlph():
            y=list()
            for i in range(20):
                y.append(str(i))       
            for j in range(10):
                x=list()
                for i in range(20):
                    x.append(str(j))
                axs.scatter(x, y, color='blue',s=4)
        iniciarAlph()

        def cargarPermut(permut):
            for i in range(len(permut)):
                for j in range(20):
                    matrixAlph[i][j]=(int(permut[i])+matrixAlph[i][j])%26
        cargarPermut(permut)

        def annotatePlot():
            for i in range(10):
                for j in range(20):
                    axs.annotate(' '+chr(matrixAlph[i][j]+97),(i,j), horizontalalignment='left', verticalalignment='center')
        annotatePlot()

        frame= LabelFrame(self)
        frame.place(x=400, y=300)
        frame.configure(width=200, height=200)

        canvas = FigureCanvasTkAgg(fig, master = frame) 
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0)


        

        def graficarGrafo(x, y):
            n=10
            vect=None
            if(self.combo.get()=='Grafo 2'):
                vect=grafo2(x, y, n)
            else:
                edges = set()
                curr = (x, y)
                for i in range(n + 1):
                    next = (curr[0] + 1, curr[1] + i)
                    segment = (curr, next)
                    curr = next
                    edges.add(segment)
                dirA = edges
                edges = set()
                for segment in dirA:
                    last = segment[1]
                    edgetm = set()
                    curr = (*last, n)
                    for i in range(n + 1):
                        next = (curr[0] + 1, curr[1] + i)
                        segment = (curr, next)
                        curr = next
                        edgetm.add(segment)
                    temp = edgetm
                    edges = edges.union(temp)
                dirB = edges
                edges = set()
                for segment in dirB:
                    last = segment[1]
                    pendiente = segment[1][1] - segment[0][1]
                    edgetm = set()
                    curr = (*last, pendiente)
                    for i in range(n + 1):
                        next = (curr[0] + 1, curr[1] + i)
                        segment = (curr, next)
                        curr = next
                        edgetm.add(segment)
                    temp = edgetm
                    edges = edges.union(temp)
                dirC = edges
                total = set()
                vect = ((total.union(dirA)).union(dirB)).union(dirC)
            return vect


        def grafo2(x, y, n):
            if((x+y)!=0):
                x=0
                y=0
            if n == 0:
                return {((x, y), (x + 1, y))}
            else:
                last = grafo2(x, y, n - 1)
                borde = set([segmento for segmento in last if segmento[1][0] == n])
                minimo = min([i[1][1] for i in borde])
                temp = set()
                for segmento in borde:
                    head = segmento[0]
                    tail = segmento[1]
                    pendiente = tail[1] - head[1]
                    if n % 2 == 1 or tail[1] > minimo:
                        temp.add((tail, (tail[0] + 1, tail[1])))
                    temp.add((tail, (tail[0] + 1, tail[1] + pendiente + 1)))
            return last.union(temp)

        

        fig2 = Figure(figsize=(4.6, 4.6), dpi=100)
        fig2.suptitle('Grafo')
        a=fig2.add_subplot(111)

        def crearGrafo(x,y,mode):
            vect= graficarGrafo(x, y)
            #plt.axis('equal')
            a.set_xlim([x, x + 15])
            a.set_ylim([y, y + 20])
            a.spines['bottom'].set_position('zero')
            a.spines['left'].set_position('zero')
            a.spines['top'].set_visible(False)
            a.spines['right'].set_visible(False)
            a.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
            a.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)
            a.set_xticks(np.arange(-10, 20 + 1), minor=True)
            a.set_yticks(np.arange(-10, 20 + 1), minor=True)
            a.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
            for segment in vect:
                p0 = segment[0]
                p1 = segment[1]
                if(mode==1):
                    xs = [p0[0]+x, p1[0]+x]
                    ys = [p0[1]+y, p1[1]+y]
                else:
                    xs = [p0[0] , p1[0] ]
                    ys = [p0[1] , p1[1] ]
                a.plot(xs, ys, color='r', linestyle="-", marker='o',
                        linewidth=1, markersize=2)
        crearGrafo(0,0,0)

        frame2= LabelFrame(self)
        frame2.place(x=870, y=300)
        frame2.configure(width=400, height=400)

        canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas2, frame2)
        toolbar.update()


        def obtenerVector(x,y):
            n=10
            if self.combo.get() == 'Grafo 1':
                edges = set()
                curr = (x, y)
                for i in range(n + 1):
                    next = (curr[0] + 1, curr[1] + i)
                    segment = (curr, next)
                    curr = next
                    edges.add(segment)
                dirA = edges
                edges = set()
                for segment in dirA:
                    last = segment[1]
                    edgetm = set()
                    curr = (*last, n)
                    for i in range(n + 1):
                        next = (curr[0] + 1, curr[1] + i)
                        segment = (curr, next)
                        curr = next
                        edgetm.add(segment)
                    temp = edgetm
                    edges = edges.union(temp)
                dirB = edges
                edges = set()
                for segment in dirB:
                    last = segment[1]
                    pendiente = segment[1][1] - segment[0][1]
                    edgetm = set()
                    curr = (*last, pendiente)
                    for i in range(n + 1):
                        next = (curr[0] + 1, curr[1] + i)
                        segment = (curr, next)
                        curr = next
                        edgetm.add(segment)
                    temp = edgetm
                    edges = edges.union(temp)
                dirC = edges
                total = set()
                vect = ((total.union(dirA)).union(dirB)).union(dirC)
            else:
                vect = grafo2(x,y,n)
            return vect


        def contador(x,y,path):            
            count = 0
            for segment in path:
                if (x,y) == segment[1]:
                    count += 1
            return count

        def aumentarAlph(x,y):
            pathh = obtenerVector(x, y)
            for i in range(10):
                for j in range(20):
                    n = contador(i,j, pathh) # n es lo que se desplaza
                    matrixAlph[i][j] = (matrixAlph[i][j]+n)%26


        #funciones para los botones
        def cifrar():
            text=texto.get("1.0","end-1c").replace(" ","").replace("\n","").lower()

            if (not text.isalpha()) and not text.split(" ")==['']:
                    messagebox.showinfo("Advertencia","S??lo se admiten letras en el texto.")
                    main_window.deiconify()
            try:
                cifrado=""
                text=list(text)
                k=len(text)
                while k > 0:
                    for i in range(10):
                        for j in range(20):
                            if(chr(matrixAlph[i][j]+97)==text[len(text)-k]):
                                cifrado+=('('+str(i)+','+str(j)+');')
                                k-=1
                            if(k==0):
                                break
                        if(k==0):
                            break
                
                resultado.configure(state='normal')
                resultado.delete("1.0", END)
                resultado.insert(INSERT, cifrado[:-1])
                resultado.configure(state='disabled')

            except:
                messagebox.showinfo("Advertencia","Hay un error con el texto.")
                main_window.deiconify()
                           

        def descifrar():
            try:
                text=texto.get("1.0","end-1c").split(";")
                descifrado = ""
                for coord in text:
                    coords = coord.split(',')
                    descifrado+=chr(matrixAlph[int(coords[0][1:])][int(coords[1][:-1])]+97)

                resultado.configure(state='normal')
                resultado.delete("1.0", END)
                resultado.insert(INSERT, descifrado)
                resultado.configure(state='disabled')
            except:
                messagebox.showinfo("Advertencia","No es posible descifrar el texto. Compruebe que el formato es correcto.")
                main_window.deiconify()
            
        def copiar_al_portapapeles():
            self.clipboard_clear()
            self.clipboard_append(resultado.get("1.0","end-1c"))

        def pegar():
            texto.delete("1.0", END)
            texto.insert(INSERT, self.clipboard_get())

        def generarclave():
            clave.delete("1.0", END)
            clave.insert(1.0,"4-8-9-5-7-6-3-1-2-0")
   
        def limpiar():
            resultado.configure(state='normal')
            resultado.delete("1.0", END)
            resultado.configure(state='disabled')
            texto.delete("1.0", END)

        botonesFrame = Frame(cifrarFrame, border=0,padx=5,pady=5,bg="black")
        botonesFrame.grid(row=2, column=0)

        botonesFrame2 = Frame(cifrarFrame, border=0,padx=5,pady=5,bg="black")
        botonesFrame2.grid(row=2, column=1)
        
        #espaciado entre botones
        for i in range(2):
            botonesFrame2.columnconfigure((0,i), weight=1, pad=30)
        for i in range(3):
            botonesFrame.columnconfigure((0,i), weight=1, pad=25)

        botonCifrar =Button(botonesFrame, command=cifrar, text="Cifrar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonCifrar.grid(row=0,column=0)

        botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5
                               ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonDescifrar.grid(row=0,column=1)  

        botonPegar =Button(botonesFrame, command=pegar, text="Pegar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonPegar.grid(row=0,column=2)       

        botonLimpiar =Button(botonesFrame2, command=limpiar, text="Limpiar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonLimpiar.grid(row=0,column=0)

        botonCopiar =Button(botonesFrame2, command=copiar_al_portapapeles, text="Copiar", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonCopiar.grid(row=0,column=1)
        
        botonGenerarClave=Button(botonesFrame2, command=generarclave, text="Generar Permutaci??n", padx=5, pady=5,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonGenerarClave.grid(row=0,column=3)


    def seleccion(self, event):
        if (self.combo.get()=="Hill para Imagen"):
            self = CriptoSistemasImagen(mainWindow)
            self.combo.current(6)



class CriptoLlave(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.mainWindow=main_window
        main_window.title("Criptosistemas de Llave P??blica")
        main_window.configure(width=1300, height=500,bg="black")
        main_window.iconbitmap('moon.ico')
        main_window.resizable(0, 0)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1300, height=500)

        self.imagespace = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrames = LabelFrame(self)
        imageLabelFrames.place(x=0, y=0)
        imageLabelFrames.configure(width=3000, height=3000)
        imageLabels = Label(imageLabelFrames, image=self.imagespace)
        imageLabels.place(x=200, y=200, anchor="center")


        self.opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5,bg="black",fg="white")
        self.opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(self.opcionesCifrado, text="Cifrador: ", padx=5, pady=5,bg="black",fg="white")
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(self.opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["RSA", "ELGAMAL", "MV", "RABIN"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)
        self.combo.current(0)

        primo1Label = Label(self.opcionesCifrado, text="Primo 1: ", padx=5, pady=5,bg="black",fg="white")
        primo1Label.grid(row=1, column=0)

        primo1Texto = Text(self.opcionesCifrado)
        primo1Texto.grid(row=1, column=1, sticky=W)
        primo1Texto.configure(height=1,width=16, padx=5, pady=5)

        self.primo2Label = Label(self.opcionesCifrado, text="Primo 2: ", padx=5, pady=5,bg="black",fg="white")
        self.primo2Label.grid(row=2, column=0)

        self.primo2Texto = Text(self.opcionesCifrado)
        self.primo2Texto.grid(row=2, column=1, sticky=W)
        self.primo2Texto.configure(height=1,width=16, padx=5, pady=5)

        def generarPrimo():
            self.botonGenerarClave.invoke()
            if self.combo.get()=="RSA":
                try:
                    primo1Texto.insert(1.0,"")
                    primo1=generatePrime()
                    primo1Texto.insert(1.0, primo1)

                    self.primo2Texto.insert(1.0,"")
                    primo2=generatePrime()
                    self.primo2Texto.insert(1.0, primo2)
                except:
                    messagebox.showinfo("Advertencia","No se han podido generar los n??meros.")
                    main_window.deiconify()


            elif self.combo.get()=="ELGAMAL":
                try:
                    primo1Texto.insert(1.0,"")
                    primo1=generatePrime()
                    primo1Texto.insert(1.0, primo1)
                except:
                    messagebox.showinfo("Advertencia","No se ha podido generar el n??mero.")
                    main_window.deiconify()
            
            elif self.combo.get()=="MV":
                try:
                    primo1Texto.insert(1.0,"")
                    primo1=randprime(100,1000)
                    primo1Texto.insert(1.0, primo1)
                except:
                    messagebox.showinfo("Advertencia","No se ha podido generar el n??mero.")
                    main_window.deiconify()

            elif self.combo.get()=="RABIN":
                try:
                    p,q=generateDataRabin()
                    primo1Texto.insert(1.0, p)
                    self.primo2Texto.insert(1.0, q)
                except:
                    messagebox.showinfo("Advertencia","No se ha podido generar el n??mero.")
                    main_window.deiconify()


        def aplicarDatos():
            if self.combo.get()=="RSA":
                try:
                    primo1= int(primo1Texto.get("1.0","end-1c"))
                    primo2= int(self.primo2Texto.get("1.0","end-1c"))
                    e,n = generateRsaData(primo1, primo2)
                    texto1.configure(state="normal")
                    texto1.insert(INSERT, e)
                    texto1.configure(state="disabled")
                    texto2.configure(state="normal")
                    texto2.insert(INSERT, n)
                    texto2.configure(state="disabled")
                except:
                    messagebox.showinfo("Advertencia","Los campos deben corresponder a n??meros primos.")
                    main_window.deiconify()
            
            elif self.combo.get()=="ELGAMAL":
                try:
                    primo1= int(primo1Texto.get("1.0","end-1c"))
                    alpha, a, alpha_a = generateGamalData(primo1)
                    texto1.configure(state="normal")
                    texto1.insert(INSERT, primo1)
                    texto1.configure(state="disabled")
                    texto2.configure(state="normal")
                    texto2.insert(INSERT, alpha)
                    texto2.configure(state="disabled")
                    self.texto3.configure(state="normal")
                    self.texto3.insert(INSERT, alpha_a)
                    self.texto3.configure(state="disabled")

                except:
                    messagebox.showinfo("Advertencia","El campo debe corresponder a un n??mero primo.")
                    main_window.deiconify()
            
            elif self.combo.get()=="MV":
                try:
                    primo1= primo1Texto.get("1.0","end-1c")
                    a,b,p,gx, gy, Ka, Nb = generateDataMV(primo1)
                    texto1.configure(state="normal")
                    texto1.insert(INSERT, a)
                    texto1.configure(state="disabled")
                    texto2.configure(state="normal")
                    texto2.insert(INSERT, b)
                    texto2.configure(state="disabled")
                    self.texto3.configure(state="normal")
                    self.texto3.insert(INSERT, p)
                    self.texto3.configure(state="disabled")
                    self.textoX.configure(state="normal")
                    self.textoX.insert(INSERT, gx)
                    self.textoX.configure(state="disabled")
                    self.textoY.configure(state="normal")
                    self.textoY.insert(INSERT, gy)
                    self.textoY.configure(state="disabled")

                except:
                    messagebox.showinfo("Advertencia","El campo debe corresponder a un n??mero primo.")
                    main_window.deiconify()

            elif self.combo.get()=="RABIN":
                pass

        botonGenerar =Button(self.opcionesCifrado, command=generarPrimo, text="Generar Primo(s)", padx=5, pady=5
                            ,font=('Comic Sans MS', 12, 'bold'), fg='black',bd='1')
        botonGenerar.grid(row=3,column=0)

        self.botonAplicar =Button(self.opcionesCifrado, command=aplicarDatos, text="Generar Datos", padx=5, pady=5
                            ,font=('Comic Sans MS', 12, 'bold'), fg='black',bd='1')
        self.botonAplicar.grid(row=3,column=1)


        self.generadoFrame = LabelFrame(self, text="Datos Generados", padx=5, pady=5,bg="black",fg="white")
        self.generadoFrame.place(x=330,y=30)
        
        texto1 = Text(self.generadoFrame)
        texto1.grid(row=0, column=1, sticky=W)
        texto1.configure(height=1,width=16, padx=5, pady=5,state="disabled")

        self.texto1Label = Label(self.generadoFrame, text="e", font=(2), padx=5, pady=5,bg="black",fg="white")
        self.texto1Label.grid(row=0, column=0)

        texto2 = Text(self.generadoFrame)
        texto2.grid(row=1, column=1, sticky=W)
        texto2.configure(height=1,width=16, padx=5, pady=5,state="disabled")

        self.texto2Label = Label(self.generadoFrame, text="n", font=(2), padx=5, pady=5,bg="black",fg="white")
        self.texto2Label.grid(row=1, column=0)

        self.texto3 = Text(self.generadoFrame)
        self.texto3.grid(row=2, column=1, sticky=W)
        self.texto3.configure(height=1,width=16, padx=5, pady=5,state="disabled")
        
        self.texto3Label = Label(self.generadoFrame, text="", padx=5, pady=5,bg="black",fg="white")
        self.texto3Label.grid(row=2, column=0)
        

        self.textoX = Text(self.generadoFrame)
        self.textoX.grid(row=3, column=1, sticky=W)
        self.textoX.configure(height=1,width=16, padx=5, pady=5,state="disabled")
        

        self.textoXLabel = Label(self.generadoFrame, text="", padx=5, pady=5,bg="black",fg="white")
        self.textoXLabel.grid(row=3, column=0)

        self.textoY = Text(self.generadoFrame)
        self.textoY.grid(row=3, column=3, sticky=W)
        self.textoY.configure(height=1,width=16, padx=5, pady=5,state="disabled")

        self.textoYLabel = Label(self.generadoFrame, text="", padx=5, pady=5,bg="black",fg="white")
        self.textoYLabel.grid(row=3, column=2)


        def limpiarValores():
            primo1Texto.configure(state='normal')
            primo1Texto.delete("1.0", END)
            texto1.configure(state='normal')
            texto1.delete("1.0", END)
            texto2.configure(state='normal')
            texto2.delete("1.0", END)   
            try:
                self.primo2Texto.configure(state='normal')
                self.primo2Texto.delete("1.0", END)
            except:
                pass
            try:
                self.texto3.configure(state='normal')
                self.texto3.delete("1.0", END)
            except:
                pass
            try:
                self.textoX.configure(state='normal')
                self.textoX.delete("1.0", END)
            except:
                pass
            try:
                self.textoY.configure(state='normal')
                self.textoY.delete("1.0", END)
            except:
                pass


        cifrarFrame = LabelFrame(self, text="Cifrar",bg="black",fg="white")
        cifrarFrame.place(x=30, y=180)

        ctClaro = Label(cifrarFrame, text="Texto",bg="black",fg="white")
        ctClaro.grid(row=0, sticky=W)

        ctCifrado = Label(cifrarFrame, text="Resultado",bg="black",fg="white")
        ctCifrado.grid(row=0, column=1, sticky=W, padx=4, pady=2)

        texto=Text(cifrarFrame)
        texto.grid(row=1,column=0, padx=4, pady=2)
        texto.configure(height=10,width=25, bg="light yellow", foreground="#000000")

        resultado=Text(cifrarFrame)
        resultado.grid(row=1,column=1, padx=4, pady=2)
        resultado.configure(height=10,width=25, bg="light cyan", foreground="#000000", state="disabled")
        

        #funciones para los botones
        def cifrar():
            if self.combo.get()=="RSA":
                try: 
                    primo1= int(primo1Texto.get("1.0","end-1c"))
                    primo2= int(self.primo2Texto.get("1.0","end-1c"))
                    text=texto.get("1.0","end-1c")
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, "----".join(RsaCifrar(text,primo1,primo2)))
                    resultado.configure(state='disabled')
                except:           
                    messagebox.showinfo("Advertencia","Hay un error con el texto o la clave no ha sido proporcionada ni generada.")
                    main_window.deiconify()

            elif self.combo.get()=="ELGAMAL":
                try:
                    primo1 = int(primo1Texto.get("1.0","end-1c"))
                    text=texto.get("1.0","end-1c")
                    alpha=int(texto2.get("1.0","end-1c"))
                    alpha_a=int(self.texto3.get("1.0","end-1c"))
                    r = ElgamalCifrar(text,primo1,alpha_a,alpha)
                    r="----".join(r)
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, r)
                    resultado.configure(state='disabled')
                except:
                    messagebox.showinfo("Advertencia","Hay un error con el texto o la clave no ha sido proporcionada ni generada.")
                    main_window.deiconify()

            elif self.combo.get()=="MV":
                try:
                    primo1 = int(primo1Texto.get("1.0","end-1c"))
                    text=texto.get("1.0","end-1c")
                    file_in = open("public_key.txt", "r")
                    a = int(file_in.readline().rstrip())
                    b = int(file_in.readline().rstrip())
                    p = int(file_in.readline().rstrip())
                    gx = int(file_in.readline().rstrip())
                    gy = int(file_in.readline().rstrip())
                    Nb = int(file_in.readline().rstrip())
                    file_in.close()
                    file_in = open("private_key.txt", "r")
                    Ka = int(file_in.read())
                    file_in.close()
                    mv = CifrarMenezesVastone(a,b,p,gx,gy,Ka,Nb,text)
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, mv)
                    resultado.configure(state='disabled')
                except:
                    messagebox.showinfo("Advertencia","Hay un error con el texto o la clave no ha sido proporcionada ni generada.")
                    main_window.deiconify()

            elif self.combo.get()=="RABIN":
                try:
                    text=texto.get("1.0","end-1c")
                    r = cifrarRabin(text)
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, r)
                    resultado.configure(state='disabled')
                except:
                    messagebox.showinfo("Advertencia","Hay un error con el texto o la clave no ha sido proporcionada ni generada.")
                    main_window.deiconify()

                             
        def descifrar():
            if self.combo.get()=="RSA":
                try:    
                    primo1= int(primo1Texto.get("1.0","end-1c"))
                    primo2= int(self.primo2Texto.get("1.0","end-1c"))
                    text=texto.get("1.0","end-1c").split('----')
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, RsaDescifrar(text,primo1,primo2))
                    resultado.configure(state='disabled')
                except:
                    messagebox.showinfo("Advertencia","Hay un error con el texto a descifrar, asegurese que los cifrados est??n separados por ----." )
                    main_window.deiconify()


            elif self.combo.get()=="ELGAMAL":
                try:
                    text=texto.get("1.0","end-1c").split('----')
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, "".join(ElgamalDescifrar(text)))
                    resultado.configure(state='disabled')
                except:
                    messagebox.showinfo("Advertencia","Hay un error con el texto a descifrar, asegurese que los cifrados est??n separados por ----." )
                    main_window.deiconify()

            elif self.combo.get()=="MV":
                try:
                    text=list(texto.get("1.0","end-1c"))
                    text[0]='['
                    text[-1]=']'
                    text="".join(text).replace(" ",",").replace("},{","],[").replace("{","(").replace("}",")")
                    text="["+text+"]"
                    text=eval(text)
                    file_in = open("public_key.txt", "r")
                    a = int(file_in.readline().rstrip())
                    b = int(file_in.readline().rstrip())
                    p = int(file_in.readline().rstrip())
                    gx = int(file_in.readline().rstrip())
                    gy = int(file_in.readline().rstrip())
                    Nb = int(file_in.readline().rstrip())
                    file_in.close()
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, "".join(DecifradoMenezesVastone(a,b,p,Nb,text)))
                    resultado.configure(state='disabled')
                except:
                    messagebox.showinfo("Advertencia","Hay un error con el texto a descifrar, asegurese que los cifrados est??n separados por ----." )
                    main_window.deiconify()
            
            elif self.combo.get()=="RABIN":
                try:    
                    text=texto.get("1.0","end-1c")
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    r = decifrarRabin(int(text))
                    st = format(r, 'x')
                    resultado.insert(INSERT,bytes.fromhex(st).decode())
                    resultado.configure(state='disabled')
                except:
                    messagebox.showinfo("Advertencia","Hay un error con el texto a descifrar." )
                    main_window.deiconify()

        def copiar_al_portapapeles():
            self.clipboard_clear()
            self.clipboard_append(resultado.get("1.0","end-1c"))

        def pegar():
            texto.delete("1.0", END)
            texto.insert(INSERT, self.clipboard_get())
            
        def generarclave():
            pass

        def limpiar():
            resultado.configure(state='normal')
            resultado.delete("1.0", END)
            resultado.configure(state='disabled')
            texto.delete("1.0", END)

        botonesFrame = Frame(cifrarFrame, border=0,padx=5,pady=5,bg="black")
        botonesFrame.grid(row=2, column=0)

        botonesFrame2 = Frame(cifrarFrame, border=0,padx=5,pady=5,bg="black")
        botonesFrame2.grid(row=2, column=1)
        
        #espaciado entre botones
        for i in range(2):
            botonesFrame2.columnconfigure((0,i), weight=1, pad=30)
        for i in range(3):
            botonesFrame.columnconfigure((0,i), weight=1, pad=25)

        botonCifrar =Button(botonesFrame, command=cifrar, text="Cifrar", padx=5, pady=5
                            ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonCifrar.grid(row=0,column=0)

        botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5
                               ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonDescifrar.grid(row=0,column=1)  

        botonPegar =Button(botonesFrame, command=pegar, text="Pegar", padx=5, pady=5
                           ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonPegar.grid(row=0,column=2)       

        self.botonLimpiar =Button(botonesFrame2, command=limpiar, text="Limpiar", padx=5, pady=5
                             ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        self.botonLimpiar.grid(row=0,column=0)

        botonCopiar =Button(botonesFrame2, command=copiar_al_portapapeles, text="Copiar", padx=5, pady=5
                            ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        botonCopiar.grid(row=0,column=1)
        
        self.botonGenerarClave=Button(botonesFrame2, command=limpiarValores, text="Generar Clave", padx=5, pady=5
                                 ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        #self.botonGenerarClave.grid(row=0,column=3)

        instrucciones = LabelFrame(self, text="Anotaciones ",bg="black",fg="white")
        instrucciones.place(x=500, y= 30)

        instruc1=Label(instrucciones, text="1. Si va a proporcionar una clave, debe corresponder a una cadena de"
                                           " 10 d??gitos formados por 0's y 1's.",bg="black",fg='white')
        instruc1.grid(row=0, column=0, stick=W)

    def seleccion(self, event):
        self.botonGenerarClave.invoke()
        self.botonLimpiar.invoke()
        index=1
        #time.sleep(0.5)
        if (self.combo.get()=="RSA"):
                index=0
                self.primo2Label.configure(text="Primo 2: ")
                self.primo2Label.grid(row=2, column=0)
                self.primo2Texto = Text(self.opcionesCifrado)
                self.primo2Texto.grid(row=2, column=1, sticky=W)
                self.primo2Texto.configure(height=1,width=16, padx=5, pady=5)
                self.texto1Label.configure(text="e", font=(2))
                self.texto2Label.configure(text="n",font=(2))
                self.texto3Label.configure(text="")
                self.textoXLabel.configure(text="")
                self.textoYLabel.configure(text="")
                

        elif (self.combo.get()=="ELGAMAL"):
                index=1
                self.primo2Label.configure(text="")
                self.texto1Label.configure(text="p", font=(2))
                self.texto2Label.configure(text="??",font=(2))
                self.texto3Label.configure(text="??^a", font=(2))
                self.textoXLabel.configure(text="")
                self.textoYLabel.configure(text="")

        elif (self.combo.get()=="MV"):
                index=2
                self.primo2Label.configure(text="")
                self.texto1Label.configure(text="a", font=(2))
                self.texto2Label.configure(text="b",font=(2))
                self.texto3Label.configure(text="p", font=(2))
                self.textoXLabel.configure(text="gx: ", font=(2))
                self.textoYLabel.configure(text="gy: ", font=(2))

        elif (self.combo.get()=="RABIN"):
                index=3
                self.primo2Label.configure(text="Primo 2: ")
                self.texto1Label.configure(text="")
                self.texto2Label.configure(text="")
                self.texto3Label.configure(text="")
                self.textoXLabel.configure(text="")
                self.textoYLabel.configure(text="")
        self.combo.current(index)
        

class CriptoFirma(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.mainWindow = main_window
        main_window.title("Firma Digital")
        main_window.configure(width=1300, height=500,bg="black")
        main_window.iconbitmap('moon.ico')
        main_window.resizable(0, 0)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1300, height=500)

        self.imagespace = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrames = LabelFrame(self)
        imageLabelFrames.place(x=0, y=0)
        imageLabelFrames.configure(width=3000, height=3000)
        imageLabels = Label(imageLabelFrames, image=self.imagespace)
        imageLabels.place(x=200, y=200, anchor="center")


        opcionesCifrado = LabelFrame(self, text="Herramientas", padx=5, pady=5,bg="black",fg="white")
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Opci??n: ", padx=5, pady=5,bg="black",fg="white")
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Firmar", "Verificar"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)
        self.combo.current(0)

        def cargar():
            filename = askopenfilename()
            ruta.configure(state="normal")
            ruta.delete("1.0", END)
            ruta.insert(INSERT,filename)
            ruta.configure(state="disabled")
            main_window.deiconify()
        
        botonCargar =Button(opcionesCifrado, command=cargar, text="Cargar archivo", padx=5, pady=5
                            ,font=('Comic Sans MS', 12, 'bold'), fg='black',bd='1')
        botonCargar.grid(row=1,column=0)

        ruta = Text(opcionesCifrado)
        ruta.grid(row=1, column=1, sticky=W)
        ruta.configure(height=1,width=16, padx=5, pady=5, state="disabled")

        #funciones para los botones
        def cifrar():
                #try:
                    filename=ruta.get("1.0","end-1c")
                    print(filename)
                    if self.combo.get()=="Verificar":
                        if(Si.Verificar(filename)):
                            messagebox.showinfo("En hora buena","La firma corresponde al archivo. El contenido del archivo no se ha modificado")
                            main_window.deiconify()
                        else:
                            messagebox.showinfo("Advertencia","La firma no corresponde con el archivo.")
                            main_window.deiconify()
                    else:
                        bol=Si.firmar(filename)
                        if bol:
                            messagebox.showinfo("En hora buena","La firma ha sido generada.")
                            main_window.deiconify()
                        else:
                            messagebox.showinfo("Advertencia","La firma no ha sido generada.")
                            main_window.deiconify()
                #except:
                    #messagebox.showinfo("Advertencia","No se ha proporcionado correctamente un archivo.")
                    #main_window.deiconify()
            
        def limpiar():
            ruta.configure(state='normal')
            ruta.delete("1.0", END)
            ruta.configure(state='disabled')

        self.botonCifrar =Button(opcionesCifrado, command=cifrar, text="Firmar", padx=5, pady=5
                            ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        self.botonCifrar.grid(row=2,column=0)

        self.botonLimpiar =Button(opcionesCifrado, command=limpiar, text="Limpiar", padx=5, pady=5
                             ,font=('Comic Sans MS', 15, 'bold'), fg='black',bd='1')
        self.botonLimpiar.grid(row=2,column=1)

        instrucciones = LabelFrame(self, text="Anotaciones ",bg="black",fg="white")
        instrucciones.place(x=500, y= 30)

        instruc1=Label(instrucciones, text="1. Si va a proporcionar una clave, debe corresponder a una cadena de"
                                           " 10 d??gitos formados por 0's y 1's.",bg="black",fg='white')
        instruc1.grid(row=0, column=0, stick=W)


    def seleccion(self, event):
        index=0
        if (self.combo.get()=="Firmar"):
                index=0
                self.botonCifrar.configure(text="Firmar")
                self.botonLimpiar.invoke()
        elif (self.combo.get()=="Verificar"):
                self.botonCifrar.configure(text="Verificar")
                self.botonLimpiar.invoke()
                index=1
        self.combo.current(index)
    
        

class Inicial(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        #self.style = ttk.Style(self)
        #self.style.theme_use('default')
        #self.style.configure('main_window',fieldbackground="blue", bg="blue")
        main_window.title("CRIPTO MOON")
        main_window.configure(bg='black')
        main_window.configure(width=1000, height=500)
        main_window.geometry("+200+200")
        self.place(width=1000, height=500)
        main_window.iconbitmap('moon.ico')
        main_window.resizable(0, 0)

        self.image1 = ImageTk.PhotoImage(file='space.jpg')
        imageLabelFrame = LabelFrame(self)
        imageLabelFrame.place(x=0, y=0)
        imageLabelFrame.configure(width=1000, height=1000)
        imageLabel = Label(imageLabelFrame, image=self.image1)
        imageLabel.place(x=200, y=200, anchor="center")

        self.image2 = ImageTk.PhotoImage(file='criptomoon.jpeg')
        #self.image3 = ImageTk.PhotoImage(file='negro.png')
        imageLabelFrame2 = LabelFrame(self)
        imageLabelFrame2.place(x=280, y=30)
        imageLabelFrame2.configure(width=470, height=80)
        imageLabel4 = Label(imageLabelFrame2, image=self.image2)
        imageLabel4.place(x=235, y=40, anchor="center")

        clasicoFrame = LabelFrame(self, text="Cifrados Cl??sicos",font=('Arial',14,'bold'),fg='white', bg='black',padx=10, pady=5)
        clasicoFrame.place(x=200,y=200)


            #funciones para los botones
        def criptosistemas():
            ventana= tk.Toplevel()
            app = CriptoSistemas(ventana)
            app.mainloop()

        def criptoanalisis():
            ventana= tk.Toplevel()
            global app
            app = Criptoanalisis(ventana)
            app.mainloop()

        botonCriptosistemas = Button(clasicoFrame, command=criptosistemas, text="CriptoSistemas",
                                   font=('Comic Sans MS', 15, 'bold'), fg='black', padx=5, pady=5, bd=1)
        botonCriptosistemas.grid(row=0,column=0)

        espacio = Label(clasicoFrame, text="  ", bg='black')
        espacio.grid(row=0, column=1)

        botonCriptoanalisis =Button(clasicoFrame, command=criptoanalisis, text="Criptoan??lisis",font=('Comic Sans MS', 15, 'bold'),
                                    padx=5, pady=5,bd=1)
        botonCriptoanalisis.grid(row=0,column=2)

        bloqueFrame = LabelFrame(self, text="Cifrado por Bloques",font=("Arial",14,'bold'),fg='white',bg='black',padx=5, pady=5)
        bloqueFrame.place(x=600,y=200)

        def criptoBloque():
            ventana= tk.Toplevel()
            app = CriptoBloque(ventana)
            app.mainloop()

        botonCriptoBloque =Button(bloqueFrame, command=criptoBloque, text="CriptoSistemas",
                                  font=('Comic Sans MS',15,'bold'),fg='black', padx=5, pady=5,bd=1)
        botonCriptoBloque.grid(row=0,column=0)


        gammaFrame = LabelFrame(self, text="Cifrado Gamma Pentagonal",font=('Arial',14,'bold'),
                                fg='white', bg='black',padx=5, pady=5)
        gammaFrame.place(x=200,y=300)

        def criptoGamma():
            ventana= tk.Toplevel()
            app = CriptoGamma(ventana)
            app.mainloop()

        botonCriptoGamma =Button(gammaFrame, command=criptoGamma, text="Gamma pentagonal",font=('Comic Sans MS', 15, 'bold'),
                                 padx=5, pady=5)
        botonCriptoGamma.grid(row=0,column=0)

        llaveFrame = LabelFrame(self, text="Cifrado LLave P??blica",font=('Arial',14,'bold'),
                                fg='white', bg='black',padx=5, pady=5)
        llaveFrame.place(x=500,y=300)

        def criptoLLave():
            ventana= tk.Toplevel()
            app = CriptoLlave(ventana)
            app.mainloop()

        botonCriptoLlave =Button(llaveFrame, command=criptoLLave, text="Criptosistemas",font=('Comic Sans MS', 15, 'bold'),
                                 padx=5, pady=5)
        botonCriptoLlave.grid(row=0,column=0)

        def criptoFirma():
            ventana= tk.Toplevel()
            app = CriptoFirma(ventana)
            app.mainloop()

        espacio = Label(llaveFrame, text="  ", bg='black')
        espacio.grid(row=0, column=1)

        botonCriptoFirma =Button(llaveFrame, command=criptoFirma, text="Firma Digital",font=('Comic Sans MS', 15, 'bold'),
                                 padx=5, pady=5)
        botonCriptoFirma.grid(row=0,column=2)





#Inicio de la aplicaci??n
ventana= tk.Tk()
app = Inicial(ventana)
app.mainloop()
