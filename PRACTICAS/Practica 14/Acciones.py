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
        
        messagebox.showinfo("Exito","Registro exitoso")
    
    def consultar_saldo(self, ncuenta):
        if ncuenta in self.__ncuenta:
            index = self.__ncuenta.index(ncuenta)
            saldo = self.__saldo[index]
            messagebox.showinfo("Consulta de Saldo","Tu saldo es: "+ str(saldo))
        else:
            messagebox.showerror("Error", "No se encontró la cuenta")
    
    def ingresar_efectivo(self, ncuenta, ingreso):
        if ncuenta in self.__ncuenta:
            index = self.__ncuenta.index(ncuenta)
            saldo = self.__saldo[index]
            saldo += ingreso
            self.__saldo[index] = saldo
            messagebox.showinfo("Actualización de saldo","Tu saldo es:"+ str(saldo))
        else:
            messagebox.showerror("Error", "No se encontró la cuenta")
    
    def retirar_efectivo(self, ncuenta, retiro):
        if ncuenta in self.__ncuenta:
            index = self.__ncuenta.index(ncuenta)
            saldo = self.__saldo[index]
            if saldo >= retiro:
                saldo -= retiro
                self.__saldo[index] = saldo
                messagebox.showinfo("Actualización de saldo","Tu saldo es:"+ str(saldo))
            else:
                messagebox.showerror("Error", "No tienes suficiente saldo")
        else:
            messagebox.showerror("Error", "No se encontró la cuenta")
    
    def depositar_a_otra_cuenta(self, ncuenta_origen, ncuenta_destino, deposito):
        if ncuenta_origen in self.__ncuenta and ncuenta_destino in self.__ncuenta:
            index_origen = self.__ncuenta.index(ncuenta_origen)
            index_destino = self.__ncuenta.index(ncuenta_destino)
            saldo_origen = self.__saldo[index_origen]
            saldo_destino = self.__saldo[index_destino]
            if saldo_origen >= deposito:
                saldo_origen -= deposito
                saldo_destino += deposito
                self.__saldo[index_origen] = saldo_origen
                self.__saldo[index_destino] = saldo_destino
                messagebox.showinfo("Depósito completado","Tu nuevo saldo es:"+ str(saldo_origen))
            else:
                messagebox.showerror("Error", "No tienes suficiente saldo")
        else:
            messagebox.showerror("Error", "No se encontró la cuenta")