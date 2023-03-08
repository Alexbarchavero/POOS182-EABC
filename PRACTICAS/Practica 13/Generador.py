from tkinter import Tk, Frame, Label, Button, Entry, messagebox
import random
import string

class Generador:
    def __init__(self,opcNoCaracteres,opcMayusculasCaracteres):
        self.__opcNoCaracteres = opcNoCaracteres
        self.__opcMayusculasCaracteres = opcMayusculasCaracteres
    
    def creadorDePass(self):
        caracteres = string.ascii_letters + string.digits
        password = ''.join(random.choice(caracteres) for i in range(int_opcNoCaracteres))
        return messagebox.showinfo("Realizado!", "La contraseña generada es: "+password)