# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:16:32 2020

@author: morte
"""

from tkinter import *
from tkinter import ttk, font


# Gestor de geometría (grid). Ventana no dimensionable

class Aplicacion():
    __ventana=None
    __usuario=None
    __clave=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Acceso")
        
        # Establece que no se pueda modificar el tamaño de la
        # ventana. El método resizable(0,0) es la forma abreviada 
        # de resizable(width=False,height=False).
        
        self.__ventana.resizable(0,0)
        fuente = font.Font(weight='bold')
        
        # Define un widget de tipo 'Frame' (marco) que será el
        # contenedor del resto de widgets. El marco se situará 
        # en la ventana 'self.raiz' ocupando toda su extensión.
        # El marco se define con un borde de 2 píxeles y la
        # opción 'relief' con el valor 'raised' (elevado) añade
        # un efecto 3D a su borde. 
        # La opción 'relief' permite los siguientes valores:
        # FLAT (llano), RAISED (elevado), SUNKEN (hundido),
        # GROOVE (hendidura) y RIDGE (borde elevado).
        # La opción 'padding' añade espacio extra interior para
        # que los widgets no queden pegados al borde del marco.
          
        self.marco = ttk.Frame(self.__ventana, borderwidth=2,
                               relief="raised", padding=(10,10))
                               
        # Define el resto de widgets pero en este caso el primer 
        # paràmetro indica que se situarán en el widget del 
        # marco anterior 'self.marco'.
                               
        self.usuarioLbl = ttk.Label(self.marco, text="Usuario:",
                               font=fuente, padding=(5,5))
        self.contraseniaLbl = ttk.Label(self.marco, text="Contraseña:",
                               font=fuente, padding=(5,5))
                               
        # Define variables para las opciones 'textvariable' de
        # cada caja de entrada 'ttk.Entry()'.
        
        self.__usuario = StringVar()
        self.__clave = StringVar()
        self.__usuario.set('')
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.__usuario,
                                width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.__clave,
                                show="*", width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Aceptar", 
                                 padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marco, text="Cancelar", 
                                 padding=(5,5), command=quit)
        
        # Define la ubicación de cada widget en el grid.
        # En este ejemplo en realidad hay dos grid (cuadrículas):
        # Una cuadrícula de 1fx1c que se encuentra en la ventana 
        # que ocupará el Frame; y otra en el Frame de 5fx3c para
        # el resto de controles.
        # La primera fila y primera columna serán la número 0.
        # La opción 'column' indica el número de columna y la
        # opción 'row' indica el número de fila donde hay que 
        # colocar un widget. 
        # La opción 'columnspan' indica al gestor que el 
        # widget ocupará en total un número determinado de
        # columnas. Las cajas para entradas 'self.ctext1' y
        # 'self.ctext2' ocuparán dos columnas y la barra
        # de separación 'self.separ1' tres.
        
        self.marco.grid(column=0, row=0)
        self.usuarioLbl.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.contraseniaLbl.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.separ1.grid(column=0, row=3, columnspan=3)
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)

        # Establece el foco en la caja de entrada de la
        # contraseña.

        self.ctext1.focus_set()
        self.__ventana.mainloop()
    
    def aceptar(self):
        if self.__clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Contraseña:", self.ctext2.get())
        else:
            print("Acceso denegado")
            self.__clave.set("")
            self.ctext2.focus_set()

def testAPP():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    testAPP()
