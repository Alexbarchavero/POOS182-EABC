from tkinter import messagebox
class Validacion:
    def __init__(self,mail,contra,mailtb,contratb):
        self.mail = mail
        self.contra = contra
        self.mailtb = mailtb
        self.contratb = contratb
    
    def validar(self):
        if self.mailtb.get()==self.mail and self.contratb.get()==self.contra:
            messagebox.showinfo("Validacion","Datos correctos")
        else:
            messagebox.showerror("Error","Datos incorrectos")