from tkinter import *

class Ventana(object):
    __ventana=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title('Geometría de Celdas en Ventana')
        for r in range(0, 5):
            for c in range(0, 5):
                cell = Entry(self.__ventana, width=10)
                cell.grid(padx=5, pady=5, row=r, column=c)
                cell.insert(0, '({}, {})'.format(r, c))

    def ejecutar(self):
        self.__ventana.mainloop()

if __name__=='__main__':
    ventana=Ventana()
    ventana.ejecutar()

