from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Text
import tkinter as tk
from ControladorBD import *

# Instancia
c = ControladorBD()

# Funciones
def exeInsert():
    c.saveUser(Name.get(),Correo.get(),Contra.get())

def exeSelectUser():
    textBus.delete("0.0", "end")
    
    rsUser = c.consulUser(Busqueda.get())
    for user in rsUser:
        cadena = str(user[0])+" "+user[1]+" "+user[2]+" "+str(user[3])
    if(rsUser):
        textBus.insert("0.0",cadena)
    else:
        messagebox.showinfo("No encontrado","Usuario no existe en BD")


def exeSelectAll():
    users = c.mostrarUsuarios()
    if users:
        for user in users:
            cadena = f'{user[0]} {user[1]} {user[2]} {user[3]}\n'
            textConsulta.insert(tk.END, cadena)
    else:
        messagebox.showinfo("Sin datos por mostrar","No se encontraron usuarios en la BD")

w1 = Tk()
w1.title("CRUD de usuarios")
w1.geometry("640x480")

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

subBus = Label(pestana2,text="Registro",fg="blue",font=("Modern",18)).pack()
textBus = Text(pestana2, height=5, width=75)
textBus.pack()

# Pestaña 3
titu3 = Label(pestana3,text="Consultar Usuarios",fg="#8B0000",font=("Modern",18)).pack()

btnConsultar = Button(pestana3,text="Consultar",command=exeSelectAll).pack()

subtConsulta = Label(pestana3,text="Lista de usuarios",fg="dark gray",font=("Modern",18)).pack()
textConsulta = Text(pestana3, height=15, width=75)
textConsulta.pack()


panel.add(pestana1, text = "Agregar Usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")

w1.mainloop()