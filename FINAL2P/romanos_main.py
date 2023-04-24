from tkinter import *
from tkinter import ttk,Tk, Frame, StringVar, Label, Entry, Button, END, BOTTOM, TOP, BOTH
from romanos import *

# Window
w1 = Tk()
w1.title("Conversion de numeros")
ancho1 = w1.winfo_screenwidth()
alto1 = w1.winfo_screenheight()
w1_ancho = 720
w1_alto = 480
x = int((ancho1-w1_ancho)/2)
y = int((alto1-w1_alto)/2)
w1.geometry("{}x{}+{}+{}".format(w1_ancho,w1_alto,x,y))

# Frames
f1 = Frame(w1)
f1.pack(fill = BOTH, expand = True)

# Variables
romano = StringVar()
arabigo = StringVar()

# Instancia
a = romanos()

# Metodos
# Metodos
def rAa():
    roman = romano.get()
    roman = roman.upper()
    roman = roman.replace(' ', '')
    arabig = a.romano_a_arabigo(roman)
    messagebox.showinfo("Listo!",f"Tu numero romano en arabigo es: {arabig}")

def aAr():
    roman = a.arabigo_a_romano(arabigo.get())
    messagebox.showinfo("Listo!",f"Tu numero arabigo en romano es: {roman}")

# Labels y entrys
LBromano = Label(f1, text="Ingrese el numero romano:", fg="blue", font=("Century Gothic",14)).pack()
ENromano = Entry(f1, textvariable=romano)
ENromano.pack()
btnConvertirRomano = Button(f1, text="Convertir a Arabigo", font=("Century Gothic",12), command=rAa).pack()

LBarabigo = Label(f1, text="Ingrese el numero arabigo:", fg="blue", font=("Century Gothic",14)).pack()
ENarabigo = Entry(f1, textvariable=arabigo)
ENarabigo.pack()
btnConvertirArabigo = Button(f1, text="Convertir a Romano", font=("Century Gothic",12), command=aAr).pack()

# Mainloop
w1.mainloop()