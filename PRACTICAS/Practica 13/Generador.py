from tkinter import Tk, Frame, Label, Button, Entry, messagebox
import random
import string

class Generador:
    def __init__(self,Longitud,Mayus,Especial,Pass,Fortaleza):
        self.__Longitud = Longitud
        self.__Mayus = Mayus
        self.__Especial = Especial
        self.__Pass = Pass
        self.__Fortaleza = Fortaleza
    
    def creadorDePass(self):
        longitu = int(self.__Longitud.get())
        mayusc = self.__Mayus.get()
        espe = self.__Especial.get()
        
        caracteres = string.ascii_lowercase
        if mayusc:
            caracteres += string.ascii_uppercase
        if espe:
            caracteres += string.punctuation
        
        password = ''.join(random.choice(caracteres) for i in range(longitu))
        self.__Pass.set(password)
        
        fortalP = 0
        if any(c.isupper() for c in password):
            fortalP += 1
        if any(c.islower() for c in password):
            fortalP += 1
        if any(c in string.punctuation for c in password):
            fortalP += 2
        if longitu>=12:
            fortalP += 1
        
        if fortalP == 1:
            fortalF = "Muy Debil"
        elif fortalP == 2:
            fortalF = "Debil"
        elif fortalP == 3:
            fortalF = "Media"
        elif fortalP == 4:
            fortalF = "Fuerte"
        elif fortalP == 5:
            fortalF = "Muy Fuerte"
        
        self.__Fortaleza.set(fortalF)