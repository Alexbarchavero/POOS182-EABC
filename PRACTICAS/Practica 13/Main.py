"""
Crea una interfaz gráfica que genere password automáticos, solicitara al usuario la longitud
(8 caracteres por default), si quiere incluir Mayúsculas o Caracteres especiales, dentro de
las opciones que tendrá agregar una para comprobar la fortaleza del password
"""
from tkinter import Tk, Frame, Label, Button, Entry
from Generador import *

#Ventana
win1 = Tk()
win1.title("Generador de cotraseñas")
win1.geometry("640x480")

#Frame
s1 = Frame(win1,bg="#ffe4c4")
s1.pack(expand=True,fill='both')

#Labels
inicio = Label(s1,text="CREADOR DE CONTRASEÑAS")
inicio.pack()
inicio.config(font=("Century Gothic",20))
opcNoCaracteresLB = Label(s1,text="Ingrese el numero de caracteres: ")
opcNoCaracteresLB.place(x=25,y=100,width=225,height=25)
opcNoCaracteresLB.config(font=("Century Gothic",10))
opcMayusEspeLB = Label(s1,text="Desea mayusculas o caracteres especiales? (Y o N): ")
opcMayusEspeLB.place(x=25,y=200,width=350,height=25)
opcMayusEspeLB.config(font=("Century Gothic",10))

#Entrys
opcNoCaracteresEN = Entry(s1)
opcNoCaracteresEN.place(x=300,y=100,width=200,height=25)
opcMayusEspeEN = Entry(s1)
opcMayusEspeEN.place(x=400,y=200,width=200,height=25)

act = Generador(opcNoCaracteresEN, opcMayusEspeEN)

#Buttons
btnCrear = Button(s1, text="Entrar", bg="#87cefa", command=act.creadorDePass)
btnCrear.pack()

# Mainloop para la ventana
win1.mainloop()
