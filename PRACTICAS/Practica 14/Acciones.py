"""
Se requiere un programa para la administración de cuenta en caja popular, con el programa
podremos consultar saldo, ingresar efectivo, retirar efectivo y depositar a otra cuenta,
cada cuenta tiene registrados los siguientes datos: No. Cuenta, titular, edad y saldo
"""
from tkinter import messagebox

class Acciones:
    
    def __init__(self):
        self.__ncuenta = []
        self.__titular = []
        self.__edad = []
        self.__saldo = []
    
    def registrar_usuario(self,ncuenta,titular,edad,saldo):
        self.__ncuenta.append(ncuenta)
        self.__titular.append(titular)
        self.__edad.append(edad)
        self.__saldo.append(saldo)
        
        messagebox.showinfo("Exito","Registro existoso")
    
    def consultSaldo(self):
        saldo = float(self.__saldo.get())
        messagebox.showinfo("Consulta de Saldo","Tu saldo es: "+saldo)
    
    def ingresarCash(self,ingreso):
        saldo = float(self.__saldo.get())
        saldo += ingreso
        messagebox.showinfo("Actualización de saldo","Tu saldo es:"+saldo)
    
    def retirarCash(self,retiro):
        saldo = float(self.__saldo.get())
        saldo -= retiro
        messagebox.showinfo("Actualización de saldo","Tu saldo es:"+saldo)
    
    def depositar(self,deposito):
        saldo = float(self.__saldo.get())
        saldo -= deposito
        messagebox.showinfo("Deposito completado","Tu nuevo saldo es:"+saldo)