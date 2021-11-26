#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import ttk
from tkinter import *
from tkinter import Text, Tk
import tkinter as tk


class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Proyecto")
        main_window.configure(bg='blue')
        self.combo = ttk.Combobox(self,state='readonly')
        self.combo.place(x=50, y=20)
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

        #botones

print("hola")
ventana= tk.Tk()
app = Application(ventana)
app.mainloop()