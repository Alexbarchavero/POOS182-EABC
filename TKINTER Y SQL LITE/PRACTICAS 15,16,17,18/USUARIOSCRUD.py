from tkinter import *
from tkinter import ttk, messagebox, Text
import tkinter as tk
from ControladorBD import *
# Instancia
c = ControladorBD()
# Funciones
def exeInsert():
    c.saveUser(Name.get(),Correo.get(),Contra.get())

def exeSelectUser():
    textBus.delete("0.0", "end")
    rsUser = c.searchUser(Busqueda.get())
    if rsUser is not None:
        for user in rsUser:
            cadena = str(user[0])+"     "+user[1]+"     "+user[2]+"     "+str(user[3])
        if(rsUser):
            textBus.insert("0.0",cadena)
        else:
            messagebox.showinfo("Usuario inexistente","El usuario no existe en la Base de Datos")
    else:
        print("Error de NoneType")

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
w1.geometry("880x560")
panel = ttk.Notebook(w1)
panel.pack(fill = 'both', expand = 'yes')
pestana1 = Frame(panel,bg="#CEE9FF")
pestana2 = Frame(panel,bg="#C8FFCB")
pestana3 = Frame(panel,bg="#FFB7B7")
pestana4 = Frame(panel,bg="#FFC4AE")
pestana5 = Frame(panel,bg="#FFEBCE")

# Pestaña 1
titu = Label(pestana1,text="Registrar Usuarios",bg="#CEE9FF",fg="blue",font=("Century Gothic",18)).pack()
Name = tk.StringVar()
LBName = Label(pestana1,text="Nombre: ",bg="#CEE9FF").pack()
ENName = Entry(pestana1,textvariable=Name).pack()
Correo = tk.StringVar()
LBCorreo = Label(pestana1,text="Correo: ",bg="#CEE9FF").pack()
ENCorreo = Entry(pestana1,textvariable=Correo).pack()
Contra = tk.StringVar()
LBContra = Label(pestana1,text="Contraseña: ",bg="#CEE9FF").pack()
ENContra = Entry(pestana1,textvariable=Contra).pack()
btnGuardar = Button(pestana1,text="Guardar Usuario",command=exeInsert).pack()

# Pestaña 2
titu2 = Label(pestana2,text="Buscar usuario",bg="#C8FFCB",fg="green",font=("Century Gothic",18)).pack()
Busqueda = tk.StringVar()
LBid = Label(pestana2,text="Identificador de usuario",bg="#C8FFCB").pack()
ENid = Entry(pestana2,textvariable=Busqueda).pack()
btnBusqueda = Button(pestana2,text="Buscar usuario",command=exeSelectUser).pack()
subBus = Label(pestana2,text="Registro",bg="#C8FFCB",fg="green",font=("Century Gothic",18)).pack()
textBus = Text(pestana2,font=("Century Gothic",11))
textBus.pack(expand=True, fill=BOTH)

# Pestaña 3
titu3 = Label(pestana3,text="Consultar Usuarios",bg="#FFB7B7",fg="#A22B2B",font=("Century Gothic",18)).pack()
btnConsultar = Button(pestana3,text="Consultar",command=exeSelectAll).pack()
subtConsulta = Label(pestana3,text="Lista de usuarios",bg="#FFB7B7",fg="#A22B2B",font=("Century Gothic",18)).pack()
treeviewConsulta = ttk.Treeview(pestana3, columns=('Id', 'Nombre', 'Correo', 'Contraseña'),show="headings")
treeviewConsulta.heading('#0', text='Index')
treeviewConsulta.heading('Id', text='ID')
treeviewConsulta.heading('Nombre', text='Nombre')
treeviewConsulta.heading('Correo', text='Correo')
treeviewConsulta.heading('Contraseña', text='Contraseña')
treeviewConsulta.pack(expand=True, fill=BOTH)

# Pestaña 4
titu4 = Label(pestana4,text="Actualizar",bg="#FFC4AE",fg="#EC5900",font=("Century Gothic",18)).pack()
Actualizacion = tk.StringVar()
LBide = Label(pestana4,text="Identificador de usuario",bg="#FFC4AE").pack()
ENide = Entry(pestana4,textvariable=Actualizacion).pack()
Name1 = tk.StringVar()
LBName1 = Label(pestana4,text="Nombre: ",bg="#FFC4AE").pack()
ENName1 = Entry(pestana4,textvariable=Name1).pack()
Correo1 = tk.StringVar()
LBCorreo1 = Label(pestana4,text="Correo: ",bg="#FFC4AE").pack()
ENCorreo1 = Entry(pestana4,textvariable=Correo1).pack()
Contra1 = tk.StringVar()
LBContra1 = Label(pestana4,text="Contraseña: ",bg="#FFC4AE").pack()
ENContra1 = Entry(pestana4,textvariable=Contra1).pack()
btnActualizar = Button(pestana4,text="Actualizar",command=exeUpdates).pack()

# Pestaña 5
titu5 = Label(pestana5,text="Eliminar",bg="#FFEBCE",fg="#E69D00",font=("Century Gothic",18)).pack()
Eliminacion = tk.StringVar()
LBide = Label(pestana5,text="Identificador de usuario",bg="#FFEBCE").pack()
ENide = Entry(pestana5,textvariable=Eliminacion).pack()
btnEliminar = Button(pestana5,text="Eliminar",command=exeDeletes).pack()

# Nombre de las pestañas en el panel
panel.add(pestana1, text = "Añadir Usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")
panel.add(pestana5, text = "Eliminar Usuario")

w1.mainloop()