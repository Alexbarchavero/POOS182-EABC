from tkinter import Tk, Frame, Button, messagebox, Entry, Label
from Validacion import *
#1 Ventana
window = Tk()
window.title("Practica 12")
window.geometry("720x480")
#2 Secciones
s1 = Frame(window,bg="#ffe4c4")
s1.pack(expand=True,fill='both')
s2 = Frame(window,bg="#deb887")
s2.pack(expand=True,fill='both')
s3 = Frame(window,bg="#fafad2")
s3.pack(expand=True,fill='both')
#3 Etiquetas
inicio = Label(s1,text="INICIO DE SESION")
inicio.pack()
maillb = Label(s1,text="Ingrese su correo: ")
maillb.place(x=50,y=100,width=105,height=25)
contraslb = Label(s2,text="Ingrese su password: ")
contraslb.place(x=50,y=100,width=120,height=25)
#4 Entradas
mailtb = Entry(s1)
mailtb.place(x=250,y=100,width=200,height=25)
contratb = Entry(s2,show="*")
contratb.place(x=250,y=100,width=200,height=25)
#5 Instancia
mail = "121040833"
contra = "123456"
validacion = Validacion(mail, contra, mailtb, contratb)
#6 Botones
btnEntrar = Button(s3, text="Entrar", bg="#87cefa", command=validacion.validar)
btnEntrar.pack()
# Main para la ventana
window.mainloop()