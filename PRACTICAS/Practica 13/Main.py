"""
Crea una interfaz gráfica que genere password automáticos, solicitara al usuario la longitud
(8 caracteres por default), si quiere incluir Mayúsculas o Caracteres especiales, dentro de
las opciones que tendrá agregar una para comprobar la fortaleza del password
"""
from tkinter import Tk, Frame, Label, Button, Entry, messagebox
from Generador import *

#Ventana
win1 = Tk()
win1.title("Generador de cotraseñas")
win1.geometry("640x480")

#Frame
s1 = Frame(win1,bg="#ffe4c4")
s1.pack(expand=True,fill='both')
s2 = Frame(win1,bg="#ffe4c4")
s2.pack(expand=True,fill='both')

#Labels
inicio = Label(s1,text="CREADOR DE CONTRASEÑAS")
inicio.pack()
inicio.config(font=("Century Gothic",20))

longitudLB = Label(s1,text="Ingrese el numero de caracteres: ")
longitudLB.place(x=25,y=100,width=225,height=25)
longitudLB.config(font=("Century Gothic",10))


#Entrys
longitudEN = Entry(s1)
longitudEN.place(x=300,y=100,width=200,height=25)


#Buttons
btnCrear = Button(s2, text="Generar Password", bg="white")
btnCrear.config(font=("Century Gothic",14))
btnCrear.pack()

# Mainloop para la ventana
win1.mainloop()
