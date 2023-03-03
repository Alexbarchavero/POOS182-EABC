from tkinter import Tk, Frame, Button, messagebox, Entry, Label

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

mail = Label(s1,text="Ingrese su correo: ")
mail.place(x=50,y=100,width=105,height=25)

contras = Label(s2,text="Ingrese su password: ")
contras.place(x=50,y=100,width=120,height=25)

#4 Entradas
mailtb = Entry(s1)
mailtb.place(x=250,y=100,width=200,height=25)

contratb = Entry(s2)
contratb.place(x=250,y=100,width=200,height=25)

#5 Variables y metodos
mail = "121040833@gmail.com"
contra = "123456"

def validar():
    if mailtb.get()==mail and contratb.get()==contra:
        messagebox.showinfo("Validacion","Datos correctos")
    else:
        messagebox.showerror("Error","Datos incorrectos")

#5 Botones
btnEntrar = Button(s3,text="Entrar",bg="#87cefa",command = validar)
btnEntrar.pack()


# Main para la ventana
window.mainloop()