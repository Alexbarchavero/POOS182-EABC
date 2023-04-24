from tkinter import messagebox
import re

class romanos:
    def __init__(self, romano, arabigo):
        self.__romano__ = romano
        self.__arabigo__ = arabigo
    
    def romano_a_arabigo(self):
        romano = str(self.__romano__.get())
        romano = romano.upper()
        romano = romano.replace(' ','')
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
        arabigo = 0
        
        if romano=="VX":
            messagebox.showerror("Error","El numero es incorrecto")
        else:
            if re.match("^[IVXLivxl ]*$", romano):
                for i in range(len(romano)):
                    if i > 0 and romanos[romano[i]] > romanos[romano[i-1]]:
                        arabigo += romanos[romano[i]] - 2 * romanos[romano[i-1]]
                    else:
                        arabigo += romanos[romano[i]]
                if arabigo < 1 or arabigo > 50:
                    messagebox.showerror("Error", "El número romano debe ser entre I y L.")
                    return None
                else:
                    return arabigo
            else:
                messagebox.showerror("Error", "Ingrese solo caracteres válidos (I, V, X, L).")
                return None
    
    def arabigo_a_romano(self):
        arabigo = int(self.__arabigo__.get())
        if (arabigo>=1 and arabigo<=50):
            romanos = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L'}
            romano = ''
            for value, symbol in sorted(romanos.items(), reverse=True):
                while arabigo >= value:
                    romano += symbol
                    arabigo -= value
            return romano
        else:
            messagebox.showerror("Error","El numero debe estar entre 1 y 50")
