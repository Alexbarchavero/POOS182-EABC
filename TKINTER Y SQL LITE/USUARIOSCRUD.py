from tkinter import *
from tkinter import ttk
import tkinter as tk

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

btnGuardar = Button(pestana1,text="Guardar Usuario").pack()


panel.add(pestana1, text = "Agregar Usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")


w1.mainloop()