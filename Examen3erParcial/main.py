from tkinter import *
from tkinter import ttk, Tk, Frame, StringVar, Label, Entry, Button, OptionMenu, END, BOTTOM, TOP, BOTH
from acciones import *

# Window
w1 = Tk()
w1.title("Inicio")
ancho1 = w1.winfo_screenwidth()
alto1 = w1.winfo_screenheight()
w1_ancho = 1080
w1_alto = 640
x = int((ancho1-w1_ancho)/2)
y = int((alto1-w1_alto)/2)
w1.geometry("{}x{}+{}+{}".format(w1_ancho,w1_alto,x,y))
# Notebook
panel1 = ttk.Notebook(w1)
panel1.pack(fill = BOTH, expand = True)
p1 = Frame(panel1)
p2 = Frame(panel1)
p3 = Frame(panel1)
# Nombramos las pestañas en el panel
panel1.add(p1, text = "Insertar")
panel1.add(p2, text = "Actualizar")
panel1.add(p3, text = "Consultar")

# Variables
Material0 = StringVar()
Material = StringVar()
Cantidad = StringVar()

# Instancia
a = acciones()

# Metodos
def insertarDatos():
    res = messagebox.askyesno("Ingresar datos","¿Desea ingresar los datos?")
    if res:
        a.insertar(Material.get(),Cantidad.get())
    else:
        messagebox.showwarning("Advertencia","Datos no ingresados")

def actualizarDatos():
    res = messagebox.askyesno("Actualizar datos","¿Desea actualizar los datos?")
    if res:
        a.actualizar(Material0.get(),Material.get(),Cantidad.get())
    else:
        messagebox.showwarning("Advertencia","Datos no actualizados")

def consultarDatos():
    TVdatos.delete(*TVdatos.get_children())
    datos = a.consultarTodos()
    if datos:
        for i in datos:
            cadena = (i[0],i[1],i[2])
            TVdatos.insert("",END,values=cadena)
    else:
        messagebox.showinfo("Datos inexistentes","No hay datos por mostrar")

# ---------------------------------------- Insertar (Widgets) ---------------------------------------- #
t1 = Label(p1,text="Insertar datos",fg="blue",font=("Century Gothic",16))
t1.pack(side=TOP)

LBmaterial1 = Label(p1,text="Material",font=("Century Gothic",12))
LBmaterial1.pack()
ENmaterial1 = Entry(p1,textvariable=Material)
ENmaterial1.pack()
LBcantidad1 = Label(p1,text="Cantidad",font=("Century Gothic",12))
LBcantidad1.pack()
ENcantidad1 = Entry(p1,textvariable=Cantidad)
ENcantidad1.pack()

btnInsertar = Button(p1,text="Insertar",font=("Century Gothic",12),command=insertarDatos).pack()

# ---------------------------------------- Actualizar (Widgets) ---------------------------------------- #
t2 = Label(p2,text="Actualizar datos",fg="blue",font=("Century Gothic",16))
t2.pack(side=TOP)

LBmaterial0 = Label(p2,text="Ingrese el Material que desea actualizar:",font=("Century Gothic",12))
LBmaterial0.pack()
ENmaterial0 = Entry(p2,textvariable=Material0)
ENmaterial0.pack()

LBmaterial2 = Label(p2,text="Material",font=("Century Gothic",12))
LBmaterial2.pack()
ENmaterial2 = Entry(p2,textvariable=Material)
ENmaterial2.pack()
LBcantidad2 = Label(p2,text="Cantidad",font=("Century Gothic",12))
LBcantidad2.pack()
ENcantidad2 = Entry(p2,textvariable=Cantidad)
ENcantidad2.pack()

btnActualizar = Button(p2,text="Actualizar",font=("Century Gothic",12),command=actualizarDatos).pack()

# ---------------------------------------- Consultar (Widgets) ---------------------------------------- #
t3 = Label(p3,text="Consultar todos los datos",fg="blue",font=("Century Gothic",16))
t3.pack(side=TOP)

TVdatos = ttk.Treeview(p3,columns=('no','material','cantidad'),show="headings")
TVdatos.heading('#0', text="Index")
TVdatos.heading('no', text="No.")
TVdatos.heading('material', text="Material")
TVdatos.heading('cantidad', text="Cantidad")
TVdatos.pack(expand=True, fill=BOTH)

btnConsultar = Button(p3,text="Consultar",font=("Century Gothic",12),command=consultarDatos).pack()

# ---------------------------------------- mainloop ---------------------------------------- #
w1.mainloop()