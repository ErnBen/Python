from tkinter import *
import os

def abrirCalculadora():
    os.system("calc")
def abrirWord():
    os.system("start winword")
def abrirPaint():
    os.system("mspaint")
    
ventana = Tk()
ventana.title("Menu principal" ) 
ventana.config(bg="orange")
ventana.geometry("520x480")
ventana.resizable(0,0)

botonCalc = Button (text="Calculadora", command= abrirCalculadora)
botonCalc.place(x=50, y=50)
botonWord = Button (text="Lugar para docuemntos", command= abrirWord)
botonWord.place(x=50, y=100)
botonPaint = Button (text="DibujosLocosXD", command= abrirPaint)
botonPaint.place(x=50, y=150)
ventana.mainloop()