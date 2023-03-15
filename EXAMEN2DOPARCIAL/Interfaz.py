from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, DISABLED, messagebox
from Acciones import *

w1 = Tk()
w1.title("Examen 1er Parcial")
w1.geometry("720x640")

acc = Acciones()

def genMat():
    name = enName.get()
    app = enAPP.get()
    apm = enAPM.get()
    year = enY.get()
    carrera = enC.get()
    acc.generarMatri(name, app, apm, year, carrera)

f1 = Frame(w1)
f1.pack(expand=True,fill='both')

lbW = Label(f1,text="Matriculas.",font=("Arial",16))
lbW.grid(row=0, column=2, padx=10, pady=10)

lbName = Label(f1,text="Nombre: ")
lbName.grid(row=1, column=1, padx=10, pady=10)
enName = Entry(f1)
enName.grid(row=1, column=2, padx=10, pady=10)

lbAPP = Label(f1,text="Apellido Paterno: ")
lbAPP.grid(row=2, column=1, padx=10, pady=10)
enAPP = Entry(f1)
enAPP.grid(row=2, column=2, padx=10, pady=10)

lbAPM = Label(f1,text="Apellido Materno: ")
lbAPM.grid(row=3, column=1, padx=10, pady=10)
enAPM = Entry(f1)
enAPM.grid(row=3, column=2, padx=10, pady=10)

lbY = Label(f1,text="Año de nacimiento: ")
lbY.grid(row=3, column=1, padx=10, pady=10)
enY = Entry(f1)
enY.grid(row=3, column=2, padx=10, pady=10)

lbC = Label(f1,text="Carrera: ")
lbC.grid(row=4, column=1, padx=10, pady=10)
enC = Entry(f1)
enC.grid(row=4, column=2, padx=10, pady=10)

btnGenerar = Button(f1,text="Generar",command=genMat)
btnGenerar.grid(row=5, column=2, padx=10, pady=10)


w1.mainloop()