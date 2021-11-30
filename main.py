#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import stat
from tkinter import ttk
from tkinter import *
from tkinter import Text, Tk
import tkinter as tk
from tkinter import messagebox

from Cypher import*




class CriptoSistemas(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Criptosistemas Clásicos")
        main_window.configure(width=1200, height=500)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1200, height=500)

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5)
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5)
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Desplazamiento", "Afín", "Vigenere", "Sustitución","Hill","Permutación"]

        claveLabel = Label(opcionesCifrado, text="Clave: ", padx=5, pady=5)
        claveLabel.grid(row=1, column=0)

        clave=Text(opcionesCifrado)
        clave.grid(row=1,column=1, sticky=W)
        clave.configure(height=1,width=16, padx=5, pady=5)

        #flat, groove, raised, ridge, solid, or sunken
        cifrarFrame = LabelFrame(self, text="Cifrar")
        cifrarFrame.place(x=30, y=150)

        ctClaro = ttk.Label(cifrarFrame, text="Texto")
        ctClaro.grid(row=0, sticky=W)

        ctCifrado = ttk.Label(cifrarFrame, text="Resultado")
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
            password=clave.get("1.0","end-1c")
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
                elif(not int((len(password)**(0.5))**2)-len(password)==0):
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
                    messagebox.showinfo("Advertencia","Hay un error con la clave. Digite los dos números separados por una coma (',')")
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
                    if resultado.get()=="":
                        messagebox.showinfo("Hay un error con la clave. Verifique que tiene todas las letras del alfabeto sin repetirse")
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

        def copiar_al_portapapeles():
            self.clipboard_clear()
            self.clipboard_append(resultado.get("1.0","end-1c"))

        def pegar():
            texto.delete("1.0", END)
            texto.insert(INSERT, self.clipboard_get())
   
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

        instrucciones = LabelFrame(self, text="Instrucciones")
        instrucciones.place(x=510, y= 30)

        instruc1=Label(instrucciones, text="1. Para el cifrado de desplazamiento la clave debe ser un número natural.")
        instruc1.grid(row=0, column=0, stick=W)

        instruc2=Label(instrucciones, text="2. Para el cifrado afín, la clave debe componerse de dos números naturales separados por una coma.")
        instruc2.grid(row=1, column=0, stick=W)

        instruc3=Label(instrucciones, text="3. Para el cifrado Vigenere, la clave debe componerse de una cadena únicamente de letras.")
        instruc3.grid(row=2, column=0, stick=W)


class Criptoanalisis(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Herramientas Criptográficas")
        main_window.configure(width=900, height=500)
        self.place(width=900, height=500)
        self.style = ttk.Style()
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.style.theme_use('clam')

        analisis = LabelFrame(self, text="Análisis", padx=5, pady=5)
        analisis.place(x=30, y=30)

        textoCifrado=Label(analisis, text="Texto cifrado")
        textoCifrado.grid(row=0,column =0, padx=5, pady=5, sticky=W)

        ctexto= Text(analisis)
        ctexto.grid(row=1,column=0, padx=4, pady=2)
        ctexto.configure(height=6,width=40, bg="light yellow", foreground="#000000")
        
        textoPlano=Label(analisis, text="Texto plano")
        textoPlano.grid(row=2,column=0, padx=5, pady=5, sticky=W)
        
        ptexto= Text(analisis)
        ptexto.grid(row=3,column=0, padx=4, pady=2)
        ptexto.configure(height=6,width=40, bg="light cyan", foreground="#000000", state="disabled")

        botonesFrame = Frame(analisis)
        botonesFrame.grid(row=4,column=0, padx=5, pady=20)

        botonAnalisis =Button(botonesFrame, command="", text="Análisis", padx=5, pady=5)
        botonAnalisis.grid(row=0,column=0)

        self.combo = ttk.Combobox(botonesFrame,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Desplazamiento", "Afín", "Vigenere", "Sustitución","Hill","Permutación"]
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)

        tamaño= Label(botonesFrame, text="Tamaño: ")
        tamaño.grid(row=0, column=2)

        self.combo = ttk.Combobox(botonesFrame,state='readonly')
        self.combo.grid(row=0, column=3)
        self.combo.configure(height=1, width=2)
        self.combo["values"] = ["1", "2", "3", "4","5","6"]

        clave= Label(botonesFrame, text="Clave: ")
        clave.grid(row=1, column=0)

        textoClave= Text(botonesFrame)
        textoClave.grid(row=1,column=1, padx=4, pady=2)
        textoClave.configure(height=1,width=5, foreground="#000000")

        b= Label(botonesFrame, text="B: ")
        b.grid(row=1, column=2)

        textoB= Text(botonesFrame)
        textoB.grid(row=1,column=3, padx=4, pady=2)
        textoB.configure(height=1,width=5, foreground="#000000")


        #espaciado entre botones
        for i in range(3):
            botonesFrame.columnconfigure((0,i), weight=2, pad=6)
            botonesFrame.columnconfigure((1,i), weight=2, pad=6)

        lista = ttk.Treeview(self, columns=("Coincidencias"))
        lista.insert("",END,text='a', values= ("6"))

        lista.heading("#0", text="Caracter")
        lista.heading("Coincidencias", text="N° de Coincidencias")
        lista.place(x=400, y=38)
        lista.configure(height=1,width=2)

    def selection_changed(self, event):
        print("Nuevo elemento seleccionado:", combo.get())

class Criptoanalisis2(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        global window 
        window = main_window
        main_window.title("Criptoanálisis")
        main_window.configure(width=900, height=800)
        self.place(width=900, height=800)
        self.style = ttk.Style()
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.style.theme_use('clam')

        self.combo = ttk.Combobox(self,state='readonly')
        self.combo.place(x=30, y=30)
        self.combo["values"] = ["Desplazamiento", "Afín", "Vigenere", "Sustitución","Hill","Permutación"]
        self.combo.bind("<<ComboboxSelected>>", self.seleccion)

    def seleccion(self, event):
        if (self.combo.get()=="Desplazamiento"):
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
            textClave.configure(height=1,width=10, foreground="#000000", state="disabled")

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
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.style.theme_use('clam')

        clasicoFrame = LabelFrame(self, text="Opciones de Cifrado", bg='#DCDAD5',padx=5, pady=5)
        clasicoFrame.place(x=20,y=20)

            #funciones para los botones
        def criptosistemas():
            ventana= tk.Tk()
            app = CriptoSistemas(ventana)
            app.mainloop()

        def criptoanalisis():
            ventana= tk.Tk()
            app = Criptoanalisis2(ventana)
            app.mainloop()

        botonCriptosistemas =Button(clasicoFrame, command=criptosistemas, text="Criptosistemas",padx=5, pady=5)
        botonCriptosistemas.grid(row=0,column=0)

        espacio = Label(clasicoFrame, text="  ", bg='#DCDAD5')
        espacio.grid(row=0, column=1)

        botonCriptoanalisis =Button(clasicoFrame, command=criptoanalisis, text="Criptoanálisis", padx=5, pady=5)
        botonCriptoanalisis.grid(row=0,column=2)


#Inicio de la aplicación
ventana= tk.Tk()
app = Inicial(ventana)
app.mainloop()