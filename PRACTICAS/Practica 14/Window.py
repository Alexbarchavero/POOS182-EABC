from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, DISABLED
from Acciones import *

#Ventana
win1 = Tk()
win1.title("Caja Popular")
win1.geometry("720x640")
# Acciones
acciones = Acciones()
# Interfaz
frame1 = Frame(win1)
frame1.pack()


def open_registro():
    win1.withdraw()
    w2 = Toplevel(win1)
    w2.title("REGISTRO")
    w2.geometry("720x640")
    frame2=Frame(w2)
    frame2.pack(expand=True,fill='both')
    
    # Funciones
    def registrar_usuario():
        ncuenta = int(ncuenta_entry.get())
        titular = titular_entry.get()
        edad = int(edad_entry.get())
        saldo = float(saldo_entry.get())
        acciones.registrar_usuario(ncuenta, titular, edad, saldo)
    
    # Registro de usuario
    ncuenta_label = Label(frame2, text="No. Cuenta")
    ncuenta_label.grid(row=0, column=0, padx=10, pady=10)
    ncuenta_entry = Entry(frame2)
    ncuenta_entry.grid(row=0, column=1, padx=10, pady=10)
    titular_label = Label(frame2, text="Titular")
    titular_label.grid(row=1, column=0, padx=10, pady=10)
    titular_entry = Entry(frame2)
    titular_entry.grid(row=1, column=1, padx=10, pady=10)
    edad_label = Label(frame2, text="Edad")
    edad_label.grid(row=2, column=0, padx=10, pady=10)
    edad_entry = Entry(frame2)
    edad_entry.grid(row=2, column=1, padx=10, pady=10)
    saldo_label = Label(frame2, text="Saldo")
    saldo_label.grid(row=3, column=0, padx=10, pady=10)
    saldo_entry = Entry(frame2)
    saldo_entry.grid(row=3, column=1, padx=10, pady=10)
    registrar_button = Button(frame2, text="Registrar usuario", command=registrar_usuario)
    registrar_button.grid(row=4, column=1, padx=10, pady=10)
    
    def killwin2():
        w2.destroy()
        win1.deiconify()
    btnClose = Button(frame2,text="Regresar",command=killwin2)
    btnClose.grid(row=5, column=1, padx=10, pady=10)


def open_acciones():
    win1.withdraw()
    w3 =  Toplevel(win1)
    w3.title("ACCIONES")
    w3.geometry("720x640")
    frame3=Frame(w3)
    frame3.pack(expand=True,fill='both')
    
    #Funciones
    def consultar_saldo():
        ncuenta = int(ncuenta2_entry.get())
        acciones.consultar_saldo(ncuenta)

    def ingresar_efectivo():
        ncuenta = int(ncuenta3_entry.get())
        ingreso = float(ingreso_entry.get())
        acciones.ingresar_efectivo(ncuenta, ingreso)

    def retirar_efectivo():
        ncuenta = int(ncuenta4_entry.get())
        retiro = float(retiro_entry.get())
        acciones.retirar_efectivo(ncuenta, retiro)

    def depositar_a_otra_cuenta():
        ncuenta_origen = int(ncuenta_origen_entry.get())
        ncuenta_destino = int(ncuenta_destino_entry.get())
        deposito = float(deposito_entry.get())
        acciones.depositar_a_otra_cuenta(ncuenta_origen, ncuenta_destino, deposito)
    
    #Acciones
    # Consulta de saldo
    ncuenta2_label = Label(frame3, text="No. Cuenta")
    ncuenta2_label.grid(row=5, column=0, padx=10, pady=10)
    ncuenta2_entry = Entry(frame3)
    ncuenta2_entry.grid(row=5, column=1, padx=10, pady=10)
    consultar_button = Button(frame3, text="Consultar saldo", command=consultar_saldo)
    consultar_button.grid(row=6, column=1, padx=10, pady=10)

    # Ingreso de efectivo
    ncuenta3_label = Label(frame3, width=15)
    ncuenta3_label.grid(row=7, column=0, padx=10, pady=10)
    ncuenta3_label.config(text="No. Cuenta")
    ncuenta3_entry = Entry(frame3)
    ncuenta3_entry.grid(row=7, column=1, padx=10, pady=10)
    ingreso_label = Label(frame3, text="Ingreso")
    ingreso_label.grid(row=8, column=0, padx=10, pady=10)
    ingreso_entry = Entry(frame3)
    ingreso_entry.grid(row=8, column=1, padx=10, pady=10)
    ingresar_button = Button(frame3, text="Ingresar efectivo", command=ingresar_efectivo)
    ingresar_button.grid(row=9, column=1, padx=10, pady=10)

    #Retiro de efectivo
    ncuenta4_label = Label(frame3, text="No. Cuenta")
    ncuenta4_label.grid(row=10, column=0, padx=10, pady=10)
    ncuenta4_entry = Entry(frame3)
    ncuenta4_entry.grid(row=10, column=1, padx=10, pady=10)
    retiro_label = Label(frame3, text="Retiro")
    retiro_label.grid(row=11, column=0, padx=10, pady=10)
    retiro_entry = Entry(frame3)
    retiro_entry.grid(row=11, column=1, padx=10, pady=10)
    retirar_button = Button(frame3, text="Retirar efectivo", command=retirar_efectivo)
    retirar_button.grid(row=12, column=1, padx=10, pady=10)

    #Depósito a otra cuenta
    ncuenta_origen_label = Label(frame3, text="No. Cuenta origen")
    ncuenta_origen_label.grid(row=13, column=0, padx=10, pady=10)
    ncuenta_origen_entry = Entry(frame3)
    ncuenta_origen_entry.grid(row=13, column=1, padx=10, pady=10)
    ncuenta_destino_label = Label(frame3, text="No. Cuenta destino")
    ncuenta_destino_label.grid(row=14, column=0, padx=10, pady=10)
    ncuenta_destino_entry = Entry(frame3)
    ncuenta_destino_entry.grid(row=14, column=1, padx=10, pady=10)
    deposito_label = Label(frame3, text="Depósito")
    deposito_label.grid(row=15, column=0, padx=10, pady=10)
    deposito_entry = Entry(frame3)
    deposito_entry.grid(row=15, column=1, padx=10, pady=10)
    depositar_button = Button(frame3, text="Depositar a otra cuenta", command=depositar_a_otra_cuenta)
    depositar_button.grid(row=16, column=1, padx=10, pady=10)
    
    def killwin3():
        w3.destroy()
        win1.deiconify()
    btnClose = Button(frame3,text="Regresar",command=killwin3)
    btnClose.grid(row=17, column=1, padx=10, pady=10)

#Etiquetas
lbWelcome = Label(win1,text="Bienvenido\n",font=("Century Gothic",36))
lbWelcome.pack()

#Botones
btnSignUp = Button(win1,text="Registro",bg="white",command=open_registro)
btnSignUp.config(font=("Century Gothic",16))
btnSignUp.pack()

btnLogin = Button(win1,text="Acciones",bg="white",command=open_acciones)
btnLogin.config(font=("Century Gothic",16))
btnLogin.pack()

win1.mainloop()