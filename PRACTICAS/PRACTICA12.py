"""
Crea una interfaz gráfica de un login que solicite el correo del usuario y una
contraseña, si el usuario tiene acceso permitido se desplegara un mensaje de
bienvenida, en caso contrario indicar que revise sus datos, este login debe incluir
los siguientes requerimientos
1. Crea un diagrama de clases para la solución antes de comenzar a
programar
2. Debe estar programado usando tus Clases y objetos propios junto con
los de Tkinter
3. El login no debe enviar correo ni contraseña vacíos, evaluar con algún
tipo de validación e informar al usuario
4. La contraseña debe estar oculta atrás de puntos o asteriscos
"""
from tkinter import Tk, Frame, Button, messagebox
#1 Ventana
window = Tk()
window.title("Practica 12")
window.geometry("960x540")
# Main para la ventana
window.mainloop()