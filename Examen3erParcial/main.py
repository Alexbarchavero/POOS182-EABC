from tkinter import *
from tkinter import ttk, Tk, Frame, StringVar, BOTH, Label, Entry, Button, OptionMenu, END, BOTTOM
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
Material = StringVar()
Cantidad = StringVar()

# Instancia
a = acciones()

# ---------------------------------------- Insertar Widgets ---------------------------------------- #
t1 = Label(p1,text="Insertar datos",fg="blue",font=("Century Gothic",16))


# ---------------------------------------- Actualizar Widgets---------------------------------------- #
t2 = Label(p2,text="Actualizar datos",fg="blue",font=("Century Gothic",16))


# ---------------------------------------- Consultar Widgets---------------------------------------- #
t3 = Label(p3,text="Consultar todos los datos",fg="blue",font=("Century Gothic",16))


# ---------------------------------------- MAINLOOP ---------------------------------------- #
w1.mainloop()