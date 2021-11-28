#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import stat
from tkinter import ttk
from tkinter import *
from tkinter import Text, Tk
import tkinter as tk


class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Criptosistemas Clásicos")
        main_window.configure(bg='blue')
        main_window.configure(width=1000, height=500)
        self.place(width=1000, height=500)
        self.style = ttk.Style()
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        self.style.theme_use('clam')

        opcionesCifrado = LabelFrame(self, text="Opciones de Cifrado", bg='#DCDAD5',padx=5, pady=5)
        opcionesCifrado.grid(row=0,column=0, sticky=W)

        cifradorLabel = Label(opcionesCifrado, text="Cifrador: ", bg='#DCDAD5', padx=5, pady=5)
        cifradorLabel.grid(row=0, column=0)

        self.combo = ttk.Combobox(opcionesCifrado,state='readonly')
        self.combo.grid(row=0, column=1)
        self.combo["values"] = ["Desplazamiento", "Affine", "Vigenere", "Sustitución","Hill","Permutación"]

        claveLabel = Label(opcionesCifrado, text="Clave: ", bg='#DCDAD5', padx=5, pady=5)
        claveLabel.grid(row=1, column=0)

        clave=Text(opcionesCifrado)
        clave.grid(row=1,column=1, sticky=W)
        clave.configure(height=1,width=3, padx=5, pady=5)

        #flat, groove, raised, ridge, solid, or sunken
        cifrarFrame = LabelFrame(self, text="Cifrar", bg='#DCDAD5')
        cifrarFrame.grid(row=1, column=0)

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

        botonesFrame = LabelFrame(cifrarFrame, text="", bg='#DCDAD5',border=0,padx=5,pady=5)
        botonesFrame.grid(row=2, column=0)

        botonCifrar =Button(botonesFrame, command=cifrar, text="Cifrar", padx=5, pady=5)
        botonCifrar.grid(row=0,column=0)

        botonDescifrar =Button(botonesFrame, command=cifrar, text="Descifrar", padx=5, pady=5)
        botonDescifrar.grid(row=0,column=1)        

        botonLimpiar =Button(botonesFrame, command=limpiar, text="Limpiar", padx=5, pady=5)
        botonLimpiar.grid(row=0,column=3)

        botonCopiar =Button(botonesFrame, command=copiar_al_portapapeles, text="Copiar Cifrado", padx=5, pady=5)
        botonCopiar.grid(row=0,column=4)


        #self.ctCifrado = ttk.Label(cifrarFrame, text="Texto cifrado")
        #self.cifrar = ttk.Label(self, text="Cifrar")
        '''self.combo = ttk.Combobox(self,state='readonly')
        self.combo.place(x=50, y=35)
        self.combo["values"] = ["Desplazamiento", "Affine", "Vigenere", "Sustitución","Hill","Permutación"]
        main_window.configure(width=1000, height=500)
        self.place(width=1000, height=500)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground="orange", background="white")
        textocifrar=Text()
        textocifrar.configure(height=10,width=25, bg="light yellow")
        textocifrar.place(x=50, y=70)
        texto_decifrar=Text()
        texto_decifrar.place(x=250, y=70)
        texto_decifrar.configure(height = 10,width = 25,bg = "light cyan",state='disabled')
        def cifrar():
            if (self.combo.get())=="Affine" :
                texto_decifrar.configure(state='normal')
                texto_decifrar.delete("1.0", END)
                texto_decifrar.configure(state='disabled')
                if textocifrar.get("1.0","end-1c")=="hola":
                  texto_decifrar.configure(state='normal')
                  texto_decifrar.insert(INSERT,"gato")
                  texto_decifrar.configure(state='disabled')
        self.boton1 =ttk.Button(ventana, command=cifrar, text="Cifrar").place(x=50, y=250,width=100)
        '''

        #botones
ventana= tk.Tk()
app = Application(ventana)
app.mainloop()