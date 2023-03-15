from tkinter import messagebox
import random
import numbers
class Acciones:
    
    def __init__(self, name, app, apm, year, carrera):
        self.__name = name
        self.__app = app
        self.__apm = apm
        self.__year = year
        self.__carrera = carrera
            
    def generarMatri(self):
        name = str(self.__name)
        app = str(self.__app)
        apm = str(self.__apm)
        year = str(self.__year)
        carrera = str(self.__carrera)
        
        matricula = "23"
        
        matricula += year[2:4]
        matricula += name [:1]
        matricula += app [:1]
        matricula += apm [:1]
        
        n1 = random.randint(100, 999)
        matricula += str((n1))
        matricula += carrera [0:3]
        messagebox.showinfo("Matricula generada","Su matricula es: "+matricula)