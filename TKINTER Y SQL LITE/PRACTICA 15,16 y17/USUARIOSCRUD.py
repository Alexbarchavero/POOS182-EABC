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
    treeviewConsulta.delete(*treeviewConsulta.get_children())
    users = c.showUsers()
    if users:
        for user in users:
            cadena = (user[0], user[1], user[2], user[3])
            treeviewConsulta.insert("", tk.END, values=cadena)
    else:
        messagebox.showinfo("Sin datos por mostrar","No se encontraron usuarios en la BD")

def exeUpdates():
    c.updateUsers(Actualizacion.get(),Name1.get(),Correo1.get(),Contra1.get())

def exeDeletes():
    c.deleteUsers(Eliminacion.get())

w1 = Tk()
w1.title("CRUD de usuarios")
w1.geometry("960x640")
panel = ttk.Notebook(w1)
panel.pack(fill = 'both', expand = 'yes')
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

# Pestaña 1
titu = Label(pestana1,text="Registrar Usuarios",fg="blue",font=("Century Gothic",18)).pack()
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
titu2 = Label(pestana2,text="Buscar usuario",fg="green",font=("Century Gothic",18)).pack()
Busqueda = tk.StringVar()
LBid = Label(pestana2,text="Identificador de usuario").pack()
ENid = Entry(pestana2,textvariable=Busqueda).pack()
btnBusqueda = Button(pestana2,text="Buscar usuario",command=exeSelectUser).pack()
subBus = Label(pestana2,text="Registro",fg="blue",font=("Century Gothic",18)).pack()
textBus = Text(pestana2, height=5, width=75)
textBus.pack()

# Pestaña 3
titu3 = Label(pestana3,text="Consultar Usuarios",fg="#8B0000",font=("Century Gothic",18)).pack()
btnConsultar = Button(pestana3,text="Consultar",command=exeSelectAll).pack()
subtConsulta = Label(pestana3,text="Lista de usuarios",fg="black",font=("Century Gothic",18)).pack()
treeviewConsulta = ttk.Treeview(pestana3, columns=('Id', 'Nombre', 'Correo', 'Contraseña'),show="headings")
treeviewConsulta.heading('#0', text='Index')
treeviewConsulta.heading('Id', text='ID')
treeviewConsulta.heading('Nombre', text='Nombre')
treeviewConsulta.heading('Correo', text='Correo')
treeviewConsulta.heading('Contraseña', text='Contraseña')
treeviewConsulta.pack()

# Pestaña 4
titu4 = Label(pestana4,text="Actualizar",fg="#EC5900",font=("Century Gothic",18)).pack()
Actualizacion = tk.StringVar()
LBide = Label(pestana4,text="Identificador de usuario").pack()
ENide = Entry(pestana4,textvariable=Actualizacion).pack()
Name1 = tk.StringVar()
LBName1 = Label(pestana4,text="Nombre: ").pack()
ENName1 = Entry(pestana4,textvariable=Name1).pack()
Correo1 = tk.StringVar()
LBCorreo1 = Label(pestana4,text="Correo: ").pack()
ENCorreo1 = Entry(pestana4,textvariable=Correo1).pack()
Contra1 = tk.StringVar()
LBContra1 = Label(pestana4,text="Contraseña: ").pack()
ENContra1 = Entry(pestana4,textvariable=Contra1).pack()
btnActualizar = Button(pestana4,text="Actualizar",command=exeUpdates).pack()

# Pestaña 5
titu5 = Label(pestana5,text="Eliminar",fg="#E69D00",font=("Century Gothic",18)).pack()
Eliminacion = tk.StringVar()
LBide = Label(pestana5,text="Identificador de usuario").pack()
ENide = Entry(pestana5,textvariable=Eliminacion).pack()
btnEliminar = Button(pestana5,text="Eliminar",command=exeDeletes).pack()

# Nombre de las pestañas en el panel
panel.add(pestana1, text = "Añadir Usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")
panel.add(pestana5, text = "Eliminar Usuario")

w1.mainloop()