from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from ControladorBD import *

# Instancia
c = ControladorBD()

# Funciones
def exeInsert():
    c.saveUser(Name.get(),Correo.get(),Contra.get())
def exeSelectUser():
    rsUser = c.consulUser(Busqueda.get())
    for user in rsUser:
        cadena = str(user[0])+" "+user[1]+" "+user[2]+" "+str(user[3])
    if():
        print(cadena)
    else:
        messagebox.showinfo("No encontrado","Usuario no existe en BD")

w1 = Tk()
w1.title("CRUD de usuarios")
w1.geometry("500x300")

panel = ttk.Notebook(w1)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

# Pestaña 1
titu = Label(pestana1,text="Registro Usuarios",fg="blue",font=("Modern",18)).pack()

Name = tk.StringVar()
LBName = Label(pestana1,text="Nombre: ").pack()
ENName = Entry(pestana1,textvariable=Name).pack()

Correo = tk.StringVar()
LBCorreo = Label(pestana1,text="Correo: ").pack()
ENCorreo = Entry(pestana1,textvariable=Correo).pack()

Contra = tk.StringVar()
LBContra = Label(pestana1,text="Contraseña: ").pack()
ENContra = Entry(pestana1,textvariable=Contra).pack()

btnGuardar = Button(pestana1,text="Guardar Usuario",command=exeInsert).pack()

# Pestaña 2
titu2 = Label(pestana2,text="Buscar usuario",fg="green",font=("Modern",18)).pack()

Busqueda = tk.StringVar()
LBid = Label(pestana2,text="Identificador de usuario").pack()
ENid = Entry(pestana2,textvariable=Busqueda).pack()

btnBusqueda = Button(pestana2,text="Buscar usuario",command=exeSelectUser).pack()

subBus = Label(pestana2,text="Registrado",fg="blue",font=("Modern",18)).pack()
textBus = tk.Text(pestana2, height=5, width=52).pack()


panel.add(pestana1, text = "Agregar Usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")

w1.mainloop()