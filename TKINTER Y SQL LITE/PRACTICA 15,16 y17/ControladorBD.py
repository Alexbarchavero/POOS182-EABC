from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/Alejandro/Documents/GitHub/POOS182-EABC/TKINTER Y SQL LITE/PRACTICA 15,16 y17/DB usuarios.db")
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
    
    def showUsers(self):
        try:
            # Creamos la conexión con la base de datos, el cursor y la consulta
            conx = self.conexionBD()
            cursor = conx.cursor()
            SQLSelectAll = "select * from tbRegistrados"
            # Obtenemos todos los usuarios registrados en la tabla 'Registrados'
            cursor.execute(SQLSelectAll)
            usuarios = cursor.fetchall()
            # Cerramos la conexión con la base de datos
            conx.close()
            # Retornamos los valores
            return usuarios
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def updateUsers(self,ide,name,email,contra):
        if (ide == "" and (name == "" or email == "" or contra == "")):
            messagebox.showwarning("Cuidado","Campos vacíos")
        else:
            try:
                # Conexión a la base de datos
                conx = self.conexionBD()
                cursor1 = conx.cursor()
                # Actualización del registro
                conH = self.encripPass(contra)
                sqlUpdates = "UPDATE tbRegistrados SET nombre = ?, correo = ?, contra = ? WHERE id = ?"
                datos = (name, email, conH, ide)
                cursor1.execute(sqlUpdates, datos)
                # Confirmar los cambios y cerrar la conexión
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito","Datos correctamente actualizados")
            except sqlite3.OperationalError:
                print("Error de consulta")
    
    def deleteUsers(self,ide):
        if ide=="":
            messagebox.showwarning("Cuidado","Campo vacío")
        else:
            try:
                # Conexion a la base de datos
                conx = self.conexionBD()
                cursor2 = conx.cursor()
                # Eliminacion de registro
                sqlDeletes = "DELETE FROM tbRegistrados WHERE id = ?"
                # Preguntar al usuario si desea borrar el campo 
                respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro que deseas eliminar este registro?")
                if respuesta:
                    # Ejecutar la consulta SQL para eliminar el registro
                    cursor2.execute(sqlDeletes,ide)
                    # Confirmar los cambios y cerrar la conexión
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Exito","Registro eliminado")
                else:
                    # Cerrar la conexion
                    conx.close()
                    messagebox.showwarning("Advertencia","Usuario no eliminado")
            except sqlite3.OperationalError:
                print("Error de consulta")