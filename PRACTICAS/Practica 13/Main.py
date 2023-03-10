from tkinter import Tk, Frame, Label, Button, Entry, messagebox, BooleanVar,Checkbutton, StringVar, IntVar, DISABLED
from Generador import *

#Ventana
win1 = Tk()
win1.title("Generador de cotraseñas")
win1.geometry("720x640")

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

PassLB = Label(s1,text="Contraseña generada: ")
PassLB.place(x=25,y=150,width=225,height=25)
PassLB.config(font=("Century Gothic",10))

Fortaleza = IntVar()
FortalezaLB = Label(s1,text="Nivel de fortaleza:")
FortalezaLB.place(x=25,y=200,width=225,height=25)
FortalezaLB.config(font=("Century Gothic",10))

FortalezaLB2 = Label(s1,textvariable=Fortaleza)
FortalezaLB2.place(x=300,y=200,width=225,height=25)
FortalezaLB2.config(font=("Century Gothic",10))

#Entrys
Longitud = StringVar()
longitudEN = Entry(s1,textvariable=Longitud)
longitudEN.place(x=300,y=100,width=200,height=25)

Pass = StringVar()
PassEN = Entry(s1, textvariable=Pass, state=DISABLED)
PassEN.place(x=300,y=150,width=200,height=25)


#Buttons
Mayus = BooleanVar()
btnCMayus = Checkbutton(s2, text="Incluir Mayusculas?",variable=Mayus)
btnCMayus.pack()
Especial = BooleanVar()
btnCEspecial = Checkbutton(s2, text="Incluir caracteres especiales?",variable=Especial)
btnCEspecial.pack()

generator = Generador(Longitud, Mayus, Especial, Pass, Fortaleza)

btnGenerar = Button(s2, text="Generar Password", bg="white",command=generator.creadorDePass)
btnGenerar.config(font=("Century Gothic",10))
btnGenerar.pack()

# Mainloop para la ventana
win1.mainloop()
