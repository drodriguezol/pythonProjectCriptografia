#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import stat
from tkinter import ttk
from tkinter import *
from tkinter import Text, Tk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
from io import BytesIO

from Cypher import*
from Block import*
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
        main_window.title("Criptosistemas Clásicos")
        main_window.configure(width=1400, height=500)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1400, height=500)

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5)
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5)
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Desplazamiento", "Afín", "Vigenere", "Sustitución","Hill","Permutación", "Hill para Imagen"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)

        claveLabel = Label(opcionesCifrado, text="Clave: ", padx=5, pady=5)
        claveLabel.grid(row=1, column=0)

        clave=Text(opcionesCifrado)
        clave.grid(row=1,column=1, sticky=W)
        clave.configure(height=1,width=16, padx=5, pady=5)

        cifrarFrame = LabelFrame(self, text="Cifrar")
        cifrarFrame.place(x=30, y=150)

        ctClaro = Label(cifrarFrame, text="Texto")
        ctClaro.grid(row=0, sticky=W)

        ctCifrado = Label(cifrarFrame, text="Resultado")
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
                    messagebox.showinfo("Advertencia","Sólo se admiten letras en el texto.")
                    main_window.deiconify()

            elif(self.combo.get())=='Desplazamiento': 
                try:
                    password=(int(password))
                    if (password<0):
                        boolPass=False
                except:
                    boolPass=False
                if(not boolPass):
                    messagebox.showinfo("Advertencia","Sólo se admiten números naturales como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, desplazamientoCifrar(text,password))
                    resultado.configure(state='disabled')
                
            elif (self.combo.get())=="Afín" :
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
                    messagebox.showinfo("Advertencia","Hay un error con la clave. Digite los dos números separados por una coma (',').")
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
                    messagebox.showinfo("Advertencia","Sólo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, vigenereCifrar(text,password))
                    resultado.configure(state='disabled')

            elif(self.combo.get())=='Sustitución': 
                import random
                letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                if (not password.isalpha() and not password.replace(" ","")==""):
                    messagebox.showinfo("Advertencia","Sólo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    if(password==''):
                        letras = list(letras)
                        random.shuffle(letras)
                        password=''.join(letras)
                        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        clave.insert(INSERT, password)
                        messagebox.showinfo("Advertencia","La clave se ha generado automáticamente.")
                        main_window.deiconify()
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, sustitucionCifrar(text,password,letras))
                    resultado.configure(state='disabled')  

            elif(self.combo.get())=='Hill': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","Sólo se admiten letras como clave.")
                    main_window.deiconify()
                elif (not int((len(password)**0.5))**2 == len(password)):
                    messagebox.showinfo("Advertencia","El tamaño de la clave debe corresponder con un número cuadrado perfecto.")
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

            elif(self.combo.get())=='Permutación': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","Sólo se admiten letras como clave.")
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
                    messagebox.showinfo("Advertencia", "Sólo se admiten letras en el texto.")
                    main_window.deiconify()

            if (self.combo.get())=='Desplazamiento':
                try:
                    password=(int(password))
                    if (password<0):
                        boolPass=False
                except:
                    boolPass=False
                
                if(not boolPass):
                    messagebox.showinfo("Advertencia","Sólo se admiten números naturales como clave.")
                    main_window.deiconify()
                else:    
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, desplazamientoDescifrar(text,password))
                    resultado.configure(state='disabled')

            elif (self.combo.get())=="Afín" :
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
                    messagebox.showinfo("Advertencia","Hay un error con la clave. Digite los dos números separados por una coma (',').")
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
                    messagebox.showinfo("Advertencia","Sólo se admiten letras como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, vigenereDescifrar(text,password))
                    resultado.configure(state='disabled')

            elif(self.combo.get())=='Sustitución': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","Sólo se admiten letras como clave.")
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
                    messagebox.showinfo("Advertencia","Sólo se admiten letras como clave.")
                    main_window.deiconify()
                elif(not int((len(password)**(0.5))**2)-len(password)==0):
                    messagebox.showinfo("Advertencia","El tamaño de la clave debe corresponder con un número cuadrado perfecto.")
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

            elif(self.combo.get())=='Permutación': 
                if (not password.isalpha()):
                    messagebox.showinfo("Advertencia","Sólo se admiten letras como clave.")
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
            elif ((self.combo.get()) == 'Afín'):
                clave.delete("1.0", END)
                clave.insert(1.0, "5,6")
            elif ((self.combo.get()) == 'Vigenere'):
                clave.delete("1.0", END)
                clave.insert(1.0, "CIPHER")
            elif ((self.combo.get()) == 'Sustitución'):
                clave.delete("1.0", END)
                clave.insert(1.0, "XNYAHPOGZQWBTSFLRCVMUEKJDI")
            elif ((self.combo.get()) == 'Hill'):
                clave.delete("1.0", END)
                clave.insert(1.0, "LIDH")
            elif ((self.combo.get()) == 'Permutación'):
                clave.delete("1.0", END)
                clave.insert(1.0, "CFABD")

   
        def limpiar():
            resultado.configure(state='normal')
            resultado.delete("1.0", END)
            resultado.configure(state='disabled')
            texto.delete("1.0", END)

        botonesFrame = Frame(cifrarFrame, border=0,padx=5,pady=5)
        botonesFrame.grid(row=2, column=0)

        botonesFrame2 = Frame(cifrarFrame, border=0,padx=5,pady=5)
        botonesFrame2.grid(row=2, column=1)
        
        #espaciado entre botones
        for i in range(2):
            botonesFrame2.columnconfigure((0,i), weight=1, pad=30)
        for i in range(3):
            botonesFrame.columnconfigure((0,i), weight=1, pad=25)

        botonCifrar =Button(botonesFrame, command=cifrar, text="Cifrar", padx=5, pady=5)
        botonCifrar.grid(row=0,column=0)

        botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5)
        botonDescifrar.grid(row=0,column=1)  

        botonPegar =Button(botonesFrame, command=pegar, text="Pegar", padx=5, pady=5)
        botonPegar.grid(row=0,column=2)       

        botonLimpiar =Button(botonesFrame2, command=limpiar, text="Limpiar", padx=5, pady=5)
        botonLimpiar.grid(row=0,column=0)

        botonCopiar =Button(botonesFrame2, command=copiar_al_portapapeles, text="Copiar", padx=5, pady=5)
        botonCopiar.grid(row=0,column=1)
        
        botonGenerarClave=Button(botonesFrame2, command=generarclave, text="Generar Clave", padx=5, pady=5)
        botonGenerarClave.grid(row=0,column=3)

        instrucciones = LabelFrame(self, text="Anotaciones")
        instrucciones.place(x=700, y= 30)

        instruc1=Label(instrucciones, text="1. Para el cifrado de desplazamiento la clave debe ser un número natural.")
        instruc1.grid(row=0, column=0, stick=W)

        instruc2=Label(instrucciones, text="2. Para el cifrado afín, la clave debe componerse de dos números naturales separados por una coma.")
        instruc2.grid(row=1, column=0, stick=W)

        instruc3=Label(instrucciones, text="3. Para el cifrado Vigenere, la clave debe componerse de una cadena únicamente de letras.")
        instruc3.grid(row=2, column=0, stick=W)
        
        instruc4 = Label(instrucciones,
                         text="4. Para el cifrado de sustitución, la clave es un permutacion del abecedario usual usado.")
        instruc4.grid(row=3, column=0, stick=W)
        
        instruc5 = Label(instrucciones,
                         text="5. Para el cifrado de hill, la clave es una palabra con tamaño cuadrado e invertible.")
        instruc5.grid(row=4, column=0, stick=W)
        
        instruc6 = Label(instrucciones,
                         text="6. Para el cifrado de permutación, la clave es una palabra sin simbolos repetidos.")
        instruc6.grid(row=5, column=0, stick=W)




    def seleccion(self, event):
        if (self.combo.get()=="Hill para Imagen"):
            self = CriptoSistemasImagen(mainWindow)
            self.combo.current(6)



class CriptoSistemasImagen(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Criptosistemas Clásicos")
        main_window.configure(width=1100, height=750,)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1200, height=1200)

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5)
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5)
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Desplazamiento", "Afín", "Vigenere", "Sustitución","Hill","Permutación", "Hill para Imagen"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)
        self.combo.current(6)

        labelInfo=LabelFrame(self,text="Información")
        labelInfo.place(x=300,y=30)
        labelClave = Label(labelInfo, text="Al cifrar, se generará automáticamente una clave y se guardará en el archivo key.npy dentro de la carpeta del proyecto.")
        labelClave.grid(row=0, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La imagen resultante al cifrar se guardará en el proyecto como imagenCifrada.jpg")
        labelCifrar.grid(row=1, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La imagen resultante al descifrar se guardará en el proyecto como imagen.jpg")
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


        botonesImagen = Label(self)
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
            

        botonUrl =Button(botonesImagen, command=imagenUrl, text="Cargar imagen desde Url", padx=5, pady=5)
        botonUrl.grid(row=1,column=0)

        botonCargar =Button(botonesImagen, command=imagenCargar, text="Cargar imagen desde la ruta espeficicada", padx=5, pady=5)
        botonCargar.grid(row=1,column=1)

        botonCifrar =Button(botonesImagen, command=cifrar, text="Cifrar", padx=5, pady=5)
        botonCifrar.grid(row=2,column=0)

        botonDescifrar =Button(botonesImagen, command=descifrar, text="Descifrar", padx=5, pady=5)
        botonDescifrar.grid(row=2,column=1)

        botonLimpiar =Button(botonesImagen, command=limpiar, text="Limpiar", padx=5, pady=5)
        botonLimpiar.grid(row=2,column=2)

        botonCargarUltima =Button(botonesImagen, command=cargarUltima, text="Cargar última imagen cifrada", padx=5, pady=5)
        botonCargarUltima.grid(row=1,column=2)



    def seleccion(self, event):
        index=0
        if (self.combo.get()=="Desplazamiento"):
                index=0
        elif (self.combo.get()=="Afín"):
                index=1
        elif (self.combo.get()=="Vigenere"):
                index=2
        elif (self.combo.get()=="Sustitución"):
                index=3
        elif (self.combo.get()=="Hill"):
                index=4
        elif (self.combo.get()=="Permutación"):
                index=5
        if (not self.combo.get()=="Hill para Imagen"):
            self = CriptoSistemas(mainWindow)
            self.combo.current(index)



class CriptoBloque(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        global mainWindow
        mainWindow=main_window
        main_window.title("Criptosistemas en Bloque")
        main_window.configure(width=1100, height=750,)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1200, height=1200)

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5)
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5)
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["DES", "3-DES", "AES", "S-DES"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)
        self.combo.current(0)

        modoLabel = Label(opcionesCifrado, text="Modo: ", padx=5, pady=5)
        modoLabel.grid(row=1, column=0)

        self.modo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.modo.grid(row=1, column=1)
        self.modo["values"] = ["ECB", "CBC", "CFB", "OFB"]
        self.modo.bind("<<ComboboxSelected>>", self.seleccion)
        self.modo.current(0)

        claveLabel = Label(opcionesCifrado, text="Clave: ", padx=5, pady=5)
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

        labelInfo=LabelFrame(self,text="Información")
        labelInfo.place(x=400,y=30)
        labelClave = Label(labelInfo, text="Al cifrar sin proporcionar clave, esta se generará automáticamente. El vector inicial siempre se genera automáticamente.")
        labelClave.grid(row=0, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La clave y vector inicial usados para CIFRAR se guardarán en el archivo key.txt y ivk.txt respectivamente en la carpeta del proyecto.")
        labelCifrar.grid(row=3, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="Si no se proporciona clave para descifrar, se usará la guardada en el archivo key.txt (si hay). El vector inicial será el almacenado en ivk.txt")
        labelCifrar.grid(row=4, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La imagen resultante al cifrar se guardará en el proyecto como imagenCifrada.bmp")
        labelCifrar.grid(row=1, column=0,sticky=W)
        labelCifrar = Label(labelInfo, text="La imagen resultante al descifrar se guardará en el proyecto como imagen.bmp")
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


        botonesImagen = Label(self)
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
            

        botonUrl =Button(botonesImagen, command=imagenUrl, text="Cargar imagen desde Url", padx=5, pady=5)
        botonUrl.grid(row=1,column=0)

        botonCargar =Button(botonesImagen, command=imagenCargar, text="Cargar imagen desde la ruta espeficicada", padx=5, pady=5)
        botonCargar.grid(row=1,column=1)

        botonCifrar =Button(botonesImagen, command=cifrar, text="Cifrar", padx=5, pady=5)
        botonCifrar.grid(row=2,column=0)

        botonDescifrar =Button(botonesImagen, command=descifrar, text="Descifrar", padx=5, pady=5)
        botonDescifrar.grid(row=2,column=1)

        botonLimpiar =Button(botonesImagen, command=limpiar, text="Limpiar", padx=5, pady=5)
        botonLimpiar.grid(row=2,column=2)

        botonCargarUltima =Button(botonesImagen, command=cargarUltima, text="Cargar última imagen cifrada", padx=5, pady=5)
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
        main_window.configure(width=1400, height=500)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1400, height=500)

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5)
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5)
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["DES", "3-DES", "AES", "S-DES"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)

        claveLabel = Label(opcionesCifrado, text="Clave: ", padx=5, pady=5)
        claveLabel.grid(row=1, column=0)

        clave=Text(opcionesCifrado)
        clave.grid(row=1,column=1, sticky=W)
        clave.configure(height=1,width=16, padx=5, pady=5)

        cifrarFrame = LabelFrame(self, text="Cifrar")
        cifrarFrame.place(x=30, y=150)

        ctClaro = Label(cifrarFrame, text="Texto")
        ctClaro.grid(row=0, sticky=W)

        ctCifrado = Label(cifrarFrame, text="Resultado")
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
                    messagebox.showinfo("Advertencia","Sólo se admiten letras en el texto.")
                    main_window.deiconify()

            elif(self.combo.get())=='Desplazamiento': 
                try:
                    password=(int(password))
                    if (password<0):
                        boolPass=False
                except:
                    boolPass=False
                if(not boolPass):
                    messagebox.showinfo("Advertencia","Sólo se admiten números naturales como clave.")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, desplazamientoCifrar(text,password))
                    resultado.configure(state='disabled')
                
                           

        def descifrar():
            text=texto.get("1.0","end-1c").replace(" ","").replace("\n","")
            password=clave.get("1.0","end-1c")
            boolPass=True
            if (not text.isalpha()) and not text.split(" ")==['']:
                    messagebox.showinfo("Advertencia", "Sólo se admiten letras en el texto.")
                    main_window.deiconify()

            

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

   
        def limpiar():
            resultado.configure(state='normal')
            resultado.delete("1.0", END)
            resultado.configure(state='disabled')
            texto.delete("1.0", END)

        botonesFrame = Frame(cifrarFrame, border=0,padx=5,pady=5)
        botonesFrame.grid(row=2, column=0)

        botonesFrame2 = Frame(cifrarFrame, border=0,padx=5,pady=5)
        botonesFrame2.grid(row=2, column=1)
        
        #espaciado entre botones
        for i in range(2):
            botonesFrame2.columnconfigure((0,i), weight=1, pad=30)
        for i in range(3):
            botonesFrame.columnconfigure((0,i), weight=1, pad=25)

        botonCifrar =Button(botonesFrame, command=cifrar, text="Cifrar", padx=5, pady=5)
        botonCifrar.grid(row=0,column=0)

        botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5)
        botonDescifrar.grid(row=0,column=1)  

        botonPegar =Button(botonesFrame, command=pegar, text="Pegar", padx=5, pady=5)
        botonPegar.grid(row=0,column=2)       

        botonLimpiar =Button(botonesFrame2, command=limpiar, text="Limpiar", padx=5, pady=5)
        botonLimpiar.grid(row=0,column=0)

        botonCopiar =Button(botonesFrame2, command=copiar_al_portapapeles, text="Copiar", padx=5, pady=5)
        botonCopiar.grid(row=0,column=1)
        
        botonGenerarClave=Button(botonesFrame2, command=generarclave, text="Generar Clave", padx=5, pady=5)
        botonGenerarClave.grid(row=0,column=3)

        instrucciones = LabelFrame(self, text="Anotaciones")
        instrucciones.place(x=700, y= 30)

        instruc1=Label(instrucciones, text="1. Para el cifrado de desplazamiento la clave debe ser un número natural.")
        instruc1.grid(row=0, column=0, stick=W)

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



class Criptoanalisis(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        global window
        window = main_window
        main_window.title("Criptoanálisis")
        main_window.configure(width=780, height=800)
        self.place(width=1400, height=950)
        self.style = ttk.Style()
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.style.theme_use('clam')

        self.combo = ttk.Combobox(self,state='readonly')
        self.combo.place(x=30, y=30)
        self.combo["values"] = ["Desplazamiento", "Afín", "Vigenere", "Sustitución","Hill"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)

    def seleccion(self, event):
        if (self.combo.get()=="Desplazamiento"):
            self = Criptoanalisis(window)
            self.combo.current(0)
            analisis = LabelFrame(self, text="Análisis", padx=5, pady=5)
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto cifrado")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=26,width=40, bg="light yellow", foreground="#000000")
            
            textoPlano=Label(analisis, text="Posibles Claves")
            textoPlano.grid(row=0,column=1, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=1,column=1, padx=4, pady=2)
            ptexto.configure(height=26,width=40, bg="light cyan", foreground="#000000", state="disabled")

            def analizar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                if (not text.isalpha()):
                    messagebox.showinfo("Advertencia", "Sólo se admiten letras en el texto.")
                    window.deiconify()
                else:
                    lista = desplazamientoAnalisis(text)
                    ptexto.configure(state='normal')
                    ptexto.delete("1.0", END)
                    for i in lista:
                        ptexto.insert(INSERT, i+"\n")
                    ptexto.configure(state='disabled')

            botonesFrame = Frame(analisis)
            botonesFrame.grid(row=10,column=0, padx=5, pady=20)

            botonAnalisis =Button(botonesFrame, command=analizar, text="Análisis", padx=5, pady=5)
            botonAnalisis.grid(row=4,column=0)
        
        elif (self.combo.get()=="Afín"):
            self = Criptoanalisis(window)
            self.combo.current(1)
            analisis = LabelFrame(self, text="Análisis", padx=5, pady=5)
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto cifrado")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=26,width=40, bg="light yellow", foreground="#000000")
            
            textoPlano=Label(analisis, text="Posibles Claves")
            textoPlano.grid(row=0,column=1, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=1,column=1, padx=4, pady=2)
            ptexto.configure(height=26,width=40, bg="light cyan", foreground="#000000", state="disabled")

            def analizar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                if (not text.isalpha()):
                    messagebox.showinfo("Advertencia", "Sólo se admiten letras en el texto.")
                    window.deiconify()
                else:
                    lista = affineAnalisis(text)
                    ptexto.configure(state='normal')
                    ptexto.delete("1.0", END)
                    for i in lista:
                        ptexto.insert(INSERT, i+"\n")
                    ptexto.configure(state='disabled')

            botonesFrame = Frame(analisis)
            botonesFrame.grid(row=10,column=0, padx=5, pady=20)

            botonAnalisis =Button(botonesFrame, command=analizar, text="Análisis", padx=5, pady=5)
            botonAnalisis.grid(row=4,column=0)

        elif (self.combo.get()=="Vigenere"):
            self = Criptoanalisis(window)
            self.combo.current(2)
            analisis = LabelFrame(self, text="Análisis", padx=5, pady=5)
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto cifrado")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=26,width=40, bg="light yellow", foreground="#000000")
            
            textoPlano=Label(analisis, text="Posible descifrado")
            textoPlano.grid(row=0,column=1, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=1,column=1, padx=4, pady=2)
            ptexto.configure(height=26,width=40, bg="light cyan", foreground="#000000", state="disabled")

            def analizar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                if (not text.isalpha()):
                    messagebox.showinfo("Advertencia", "Sólo se admiten letras en el texto.")
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

            botonesFrame = Frame(analisis)
            botonesFrame.grid(row=2,column=0, padx=5, pady=20)

            labelPosibleClave = Label(botonesFrame, text="Posible Clave: ")
            labelPosibleClave.grid(row=0,column=1,padx=20,pady=5)

            textClave = Text(botonesFrame)
            textClave.grid(row=0,column=2, padx=4, pady=5)
            textClave.configure(height=1,width=10, foreground="#000000", background="#FFFFFF", state="disabled")

            botonAnalisis =Button(botonesFrame, command=analizar, text="Análisis", padx=5, pady=5)
            botonAnalisis.grid(row=0,column=0)

        elif (self.combo.get()=="Sustitución"):
            self = Criptoanalisis(window)
            window.configure(width=1400, height=950)
            self.place(width=1400, height=950)
            self.combo.current(3)         
            analisis = LabelFrame(self, text="Análisis", padx=5, pady=5)
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto cifrado")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=19,width=40, bg="light yellow", foreground="#000000")

            botonesFrame = Frame(analisis)
            botonesFrame.grid(row=2,column=0, padx=5, pady=20)

            labelPosibleClave = Label(botonesFrame, text="Posible Clave: ")
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

                
            botonAnalisis =Button(botonesFrame, command=ingresarFrecuencias, text="Análisis", padx=5, pady=5)
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
                        messagebox.showinfo("Advertencia", "Sólo se admiten letras en el texto.")
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

            botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5)
            botonDescifrar.grid(row=0,column=1)
            
            textoPlano=Label(analisis, text="Posible descifrado")
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

            botonAnalisis =Button(self, command="", text="Análisis", padx=5, pady=5)
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
            analisis = LabelFrame(self, text="Análisis", padx=5, pady=5)
            analisis.place(x=30, y=60)

            textoCifrado=Label(analisis, text="Texto plano")
            textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

            ctexto= Text(analisis)
            ctexto.grid(row=1,column=0, padx=4, pady=2)
            ctexto.configure(height=26,width=40, bg="light yellow", foreground="#000000")
            
            textoPlano=Label(analisis, text="Texto cifrado")
            textoPlano.grid(row=0,column=1, padx=5, pady=5, sticky=W)
            
            ptexto= Text(analisis)
            ptexto.grid(row=1,column=1, padx=4, pady=2)
            ptexto.configure(height=26,width=40, bg="light cyan", foreground="#000000")

            def analizar():
                text=ctexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                text2=ptexto.get("1.0","end-1c").replace(" ","").replace("\n","")
                if (not text.isalpha()):
                    messagebox.showinfo("Advertencia", "Sólo se admiten letras en ambos textos.")
                    window.deiconify()
                elif (not text2.isalpha()):
                    messagebox.showinfo("Advertencia", "Sólo se admiten letras en ambos texto.")
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
                            textClave.insert(INSERT, "Una posible clave es "+ i[0] + " que corresponde a una matriz de dimensión m = "+str(i[1])+".\n")
                            textClave.configure(state='disabled')
                    except:
                        messagebox.showinfo("Advertencia", "A partir de los textos no se puede encontrar una clave.")
                        window.deiconify()
                        


            botonesFrame = Frame(analisis)
            botonesFrame.grid(row=2,column=0, padx=5, pady=20)

            labelPosibleClave = Label(analisis, text="Posibles Claves: ")
            labelPosibleClave.grid(row=3,column=0,padx=20,pady=5, sticky=W)

            labelEspacio = Label(analisis, text="")
            labelEspacio.grid(row=4,column=0,padx=20,pady=5, sticky=W)
            labelEspacio.configure(width=1,height=10)


            textClave = Text(self)
            textClave.place(x=40,y=650)
            textClave.configure(height=6,width=81, foreground="#000000", background="#FFFFFF", state="disabled")

            botonAnalisis =Button(botonesFrame, command=analizar, text="Análisis", padx=5, pady=5)
            botonAnalisis.grid(row=0,column=0)



class Inicial(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Herramientas Criptográficas")
        main_window.configure(bg='#DCDAD5')
        main_window.configure(width=500, height=500)
        self.place(width=500, height=500)
        self.style = ttk.Style()
        self.style.configure("TCombobox", fieldbackground="white", bg="white")
        self.style.theme_use('clam')

        clasicoFrame = LabelFrame(self, text="Cifrados Clásicos", bg='#DCDAD5',padx=5, pady=5)
        clasicoFrame.place(x=20,y=20)


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

        botonCriptosistemas =Button(clasicoFrame, command=criptosistemas, text="Criptosistemas",padx=5, pady=5)
        botonCriptosistemas.grid(row=0,column=0)

        espacio = Label(clasicoFrame, text="  ", bg='#DCDAD5')
        espacio.grid(row=0, column=1)

        botonCriptoanalisis =Button(clasicoFrame, command=criptoanalisis, text="Criptoanálisis", padx=5, pady=5)
        botonCriptoanalisis.grid(row=0,column=2)

        bloqueFrame = LabelFrame(self, text="Cifrado por Bloques", bg='#DCDAD5',padx=5, pady=5)
        bloqueFrame.place(x=20,y=100)

        def criptoBloque():
            ventana= tk.Toplevel()
            app = CriptoBloque(ventana)
            app.mainloop()

        botonCriptoBloque =Button(bloqueFrame, command=criptoBloque, text="CriptoSistemas",padx=5, pady=5)
        botonCriptoBloque.grid(row=0,column=0)

#Inicio de la aplicación
ventana= tk.Tk()
app = Inicial(ventana)
app.mainloop()
