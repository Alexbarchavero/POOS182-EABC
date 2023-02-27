from tkinter import *

#1. Generar una ventana
ventana = Tk()
ventana.title("Practica 11")
ventana.geometry("700x500")

#2. Agregar frames
seccion1 = Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')
seccion2 = Frame(ventana,bg="gray")
seccion2.pack(expand=True,fill='both')
seccion3 = Frame(ventana,bg="purple")
seccion3.pack(expand=True,fill='both')

#3. Agregamos botones
botonAzul = Button(seccion1,text="Button blue",fg="blue")
botonAzul.place(x=60,y=60,width=100,height=40)
botonAmarillo = Button(seccion2,text="Button yellow",bg="yellow")
botonAmarillo.grid(row=1,column=0)
botonNegro = Button(seccion2,text="Button black",fg="black")
botonNegro.grid(row=0,column=0)
botonVerde = Button(seccion3,text="Button green",fg="green")
botonVerde.pack()
#Metodo main para la ejecucion de la ventana
ventana.mainloop()