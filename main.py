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
        main_window.configure(width=1000, height=500)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.place(width=1000, height=500)

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", padx=5, pady=5)
        opcionesCifrado.place(x=30,y=30)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", padx=5, pady=5)
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Desplazamiento", "Affine", "Vigenere", "Sustitución","Hill","Permutación"]

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
        texto.configure(height=10,width=25, bg="light yellow")

        resultado=Text(cifrarFrame)
        resultado.grid(row=1,column=1, padx=4, pady=2)
        resultado.configure(height=10,width=25, bg="light cyan", state="disabled")


        #funciones para los botones
        def cifrar():
            text=texto.get("1.0","end-1c").replace(" ","")
            password=clave.get("1.0","end-1c")
            boolPass=True

            if (not text.isalpha()) and not text.split(" ")==['']:
                    messagebox.showinfo("Advertencia","Sólo se admiten letras en el texto.")
                    main_window.deiconify()

            elif(self.combo.get())=='Desplazamiento': 
                try:
                    password=(int(password))
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
                
            elif (self.combo.get())=="Affine" :
                password=password.split(",")
                if(len(password)>2):
                    boolPass=False
                try:
                    password[0]=(int(password[0]))
                    password[1]=(int(password[1]))
                except:
                    boolPass=False

                if(not boolPass):
                    messagebox.showinfo("Advertencia","Hay un error con la clave. Digite los dos números separados por una coma (',')")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, affineCifrar(text,password))
                    resultado.configure(state='disabled')

        def descifrar():
            text=texto.get("1.0","end-1c").replace(" ","")
            password=clave.get("1.0","end-1c")
            boolPass=True

            if (not text.isalpha()) and not text.split(" ")==['']:
                    messagebox.showinfo("Advertencia", "Sólo se admiten letras en el texto.")
                    main_window.deiconify()

            if (self.combo.get())=='Desplazamiento':
                try:
                    password=(int(password))
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

            elif (self.combo.get())=="Affine" :
                password=password.split(",")
                if(len(password)>2):
                    boolPass=False
                try:
                    password[0]=(int(password[0]))
                    password[1]=(int(password[1]))
                except:
                    boolPass=False

                if(not boolPass):
                    messagebox.showinfo("Advertencia","Hay un error con la clave. Digite los dos números separados por una coma (',')")
                    main_window.deiconify()
                else:
                    resultado.configure(state='normal')
                    resultado.delete("1.0", END)
                    resultado.insert(INSERT, affineDescifrar(text,password))
                    resultado.configure(state='disabled')

        def copiar_al_portapapeles():
            self.clipboard_clear()
            self.clipboard_append(resultado.get("1.0","end-1c"))

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
            botonesFrame.columnconfigure((0,i), weight=1, pad=50)
            botonesFrame2.columnconfigure((0,i), weight=1, pad=50)

        botonCifrar =Button(botonesFrame, command=cifrar, text="Cifrar", padx=5, pady=5)
        botonCifrar.grid(row=0,column=0)

        botonDescifrar =Button(botonesFrame, command=descifrar, text="Descifrar", padx=5, pady=5)
        botonDescifrar.grid(row=0,column=1)        

        botonLimpiar =Button(botonesFrame2, command=limpiar, text="Limpiar", padx=5, pady=5)
        botonLimpiar.grid(row=0,column=0)

        botonCopiar =Button(botonesFrame2, command=copiar_al_portapapeles, text="Copiar", padx=5, pady=5)
        botonCopiar.grid(row=0,column=1)
'''
        botonesFrame.grid_rowconfigure(0,weight=1000)
        botonesFrame.grid_columnconfigure(4,weight=1000)
'''
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

        botonCriptosistemas =Button(clasicoFrame, command=criptosistemas, text="Criptosistemas",padx=5, pady=5)
        botonCriptosistemas.grid(row=0,column=0)

        espacio = Label(clasicoFrame, text="  ", bg='#DCDAD5')
        espacio.grid(row=0, column=1)

        botonCriptoanalisis =Button(clasicoFrame, command=criptosistemas, text="Criptoanálisis", padx=5, pady=5)
        botonCriptoanalisis.grid(row=0,column=2)




print(desplazamientoCifrar('arroz', 1))
ventana= tk.Tk()
app = Inicial(ventana)
app.mainloop()

