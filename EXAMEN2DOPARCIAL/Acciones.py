from tkinter import messagebox
import random

class Acciones:
    
    def __init__(self, name, app, apm, year, carrera):
        self.__name = name
        self.__app = app
        self.__apm = apm
        self.__year = year
        self.__carrera = carrera
            
    def generarMatri(self, name, app, apm, year, carrera):
        name = self.__name.get()
        app = self.__app.get()
        apm = self.__apm.get()
        year = self.__year.get()
        carrera = self.__carrera.get()
        
        
        