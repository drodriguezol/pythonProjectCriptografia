#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import stat
from tkinter import ttk
from tkinter import *
from tkinter import Text, Tk
import tkinter as tk




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

        ctClaro = ttk.Label(cifrarFrame, text="Texto claro")
        ctClaro.grid(row=0, sticky=W)

        ctCifrado = ttk.Label(cifrarFrame, text="Texto cifrado")
        ctCifrado.grid(row=0, column=1, sticky=W, padx=4, pady=2)

        textoClaro=Text(cifrarFrame)
        textoClaro.grid(row=1,column=0, padx=4, pady=2)
        textoClaro.configure(height=10,width=25, bg="light yellow")

        textoCifrado=Text(cifrarFrame)
        textoCifrado.grid(row=1,column=1, padx=4, pady=2)
        textoCifrado.configure(height=10,width=25, bg="light cyan", state="disabled")


        #funciones para los botones
        def cifrar():
            if (self.combo.get())=="Affine" :
                textoCifrado.configure(state='normal')
                textoCifrado.delete("1.0", END)
                textoCifrado.configure(state='disabled')
                if textoClaro.get("1.0","end-1c")=="hola":
                  textoCifrado.configure(state='normal')
                  textoCifrado.insert(INSERT,"gato")
                  textoCifrado.configure(state='disabled')

        def copiar_al_portapapeles():
            self.clipboard_clear()
            self.clipboard_append(textoCifrado.get("1.0","end-1c"))

        def limpiar():
            textoCifrado.configure(state='normal')
            textoCifrado.delete("1.0", END)
            textoCifrado.configure(state='disabled')
            textoClaro.delete("1.0", END)

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

        botonDescifrar =Button(botonesFrame, command=cifrar, text="Descifrar", padx=5, pady=5)
        botonDescifrar.grid(row=0,column=1)        

        botonLimpiar =Button(botonesFrame2, command=limpiar, text="Limpiar", padx=5, pady=5)
        botonLimpiar.grid(row=0,column=0)

        botonCopiar =Button(botonesFrame2, command=copiar_al_portapapeles, text="Copiar Cifrado", padx=5, pady=5)
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





ventana= tk.Tk()
app = Inicial(ventana)
app.mainloop()

