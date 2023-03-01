from tkinter import Tk, Frame, Button, messagebox

#5. agregar funcion de mensaje
def mostrarMensaje():
    messagebox.showinfo("Informacion","Te informo que todo fallo con exito")
    messagebox.showerror("Error","Perdon te falle!")
    print(messagebox.askokcancel("Pregunta","Seguro que quieres guardar?"))

#6. Funcion agregar botones
def agregarboton():
    botonVerde.config(text="+",bg="gray",fg="white")
    botonNuevo = Button(seccion3, text="Boton nuevo")
    botonNuevo.pack()

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
botonAzul = Button(seccion1,text="Button blue",bg="#5aaeee",command=mostrarMensaje)
botonAzul.place(x=60,y=60,width=100,height=40)

botonAmarillo = Button(seccion2,text="Button yellow",bg="#f7db1b")
botonAmarillo.grid(row=1,column=0)

botonNegro = Button(seccion2,text="Button black",bg="#1f1f1f",fg="#ffffff")
botonNegro.grid(row=0,column=0)

botonVerde = Button(seccion3,text="Button green",bg="#64ff5e",command=agregarboton)
botonVerde.pack()


#Metodo main para la ejecucion de la ventana
ventana.mainloop()