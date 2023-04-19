from tkinter import messagebox
import sqlite3

class acciones:
    def __init__(self):
        pass
    
    def conxBD(self):
        try:
            conx = sqlite3.connect("C:/Users/Alejandro/Documents/GitHub/POOS182-EABC/Examen3erParcial/Ferretería.db")
            print("Conexion correcta")
            return conx
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def insertar(self, m, c):
        try:
            con = self.conxBD()
            if (m=="" or c==""):
                messagebox.showwarning("Campos Vacios","Ingrese los datos")
                con.close()
            else:
                c1 = con.cursor()
                datos = (m,c)
                scriptSQL = "INSERT INTO MatConstruccion (Material,Cantidad) VALUES (?, ?)"
                c1.execute(scriptSQL,datos)
                con.commit()
                con.close()
                messagebox.showinfo("Registro exitoso!","Se ha completado el registro correctamente")
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def actualizar(self, m1, m2, c):
        try:
            con = self.conxBD()
            c2 = con.cursor()
            
            def validar():
                try:
                    scriptValidar = "SELECT Material FROM MatConstruccion WHERE Material = ?"
                    c2.execute(scriptValidar,m1)
                    res = c2.fetchone()
                    if res:
                        con.commit()
                        return res
                except sqlite3.OperationalError:
                    print("Error de consulta")
            
            if(m1=="" or validar() is None):
                messagebox.showwarning("Error de datos","Datos vacios o incorrectos")
                con.close()
            else:
                datos =  (m2,c)
                scriptSQL = "UPDATE MatConstruccion SET Material = ?, Cantidad = ?"
                c2.execute(scriptSQL,datos)
                con.commit()
                con.close()
                messagebox.showinfo("Actualizacion exitosa!","Datos correctamente actualizados")
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    #def consultarTodos(self):
        #try:
            
        #except sqlite3.OperationalError:
        #    print("Error de consulta")