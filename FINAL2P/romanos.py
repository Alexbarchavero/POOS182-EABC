from tkinter import messagebox

class romanos:
    def __init__(self):
        pass
    def romano_a_arabigo(romano):
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabigo = 0
        for i in range(len(romano)):
            if i > 0 and romanos[romano[i]] > romanos[romano[i-1]]:
                arabigo += romanos[romano[i]] - 2 * romanos[romano[i-1]]
            else:
                arabigo += romanos[romano[i]]
        return arabigo
    
    def arabigo_a_romano(arabigo):
        romanos = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        romano = ''
        for value, symbol in sorted(romanos.items(), reverse=True):
            while arabigo >= value:
                romano += symbol
                arabigo -= value
        return romano
