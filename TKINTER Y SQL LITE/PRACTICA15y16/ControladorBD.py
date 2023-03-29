from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/Alejandro/Documents/GitHub/POOS182-EABC/TKINTER Y SQL LITE/PRACTICA15y16/DB usuarios.db")
            print("Conectando a la base de datos")
            return conexion
        except sqlite3.OperationalError:
            print("No pudo hacerse la conexion")
    
    def encripPass(self,contra):
        # 1 Preparamos la contra y la sal pa la hash
        conPlana = contra
        conPlana = conPlana.encode()
        sal = bcrypt.gensalt()
        
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)
        
        return conHa
    
    def saveUser(self,name,email,contra):
        # 1 llamar metodo conexion
        conx = self.conexionBD()
        
        # 2 validar vacios
        if (name == "" or email == "" or contra == "") :
            messagebox.showwarning("Cuidado","Formulario incompleto")
            conx.close()
        else:
            # 3 Realizar insert a BD
            # 4 Preparar las variables
            cursor = conx.cursor()
            conH = self.encripPass(contra)
            datos = (name,email,conH)
            SaveInSql = "insert into tbRegistrados(nombre,correo,contra) values(?,?,?)"
            
            # 5 Ejecutar insert
            cursor.execute(SaveInSql,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Realizado","Usuario Guardado")
    
    def consulUser(self,id):
        # Realizar la conexion a la BD
        conx = self.conexionBD()
        
        # Verificar que el id no este vacio
        if id ==  '':
            messagebox.showwarning("Advertencia","Campo vacío")
            conx.close()
        else:
            # Proceder a la consulta
            try:
                cursor = conx.cursor()
                sqlSelect = " select * from tbRegistrados where id = "+id
                
                # Ejecutar
                cursor.execute(sqlSelect)
                RSuser = cursor.fetchall()
                conx.close()
                return RSuser
                
            except sqlite3.OperationalError:
                print("Error de consulta")