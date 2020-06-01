# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:55:39 2020

@author: morte
"""
from tkinter import *
from tkinter import ttk
class Aplicacion(object):
    __ventana=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry('300x200')
        self.__ventana().mainloop()


def main():
    app = Aplicacion()

if __name__=='__main__':
    main()