from PERSONAJE import *
#1. SOLICITAR DATOS
print("\n----------SOLICITUD DE DATOS DEL HEROE----------")
especieH = input("Escribe la especie del Heroe: ")
nombreH = input("Escribe el nombre del Heroe: ")
altH = float(input("Escribe la altura del Heroe: "))
recargarH = int(input("Ingresa las balas del Heroe: "))

print("\n----------SOLICITUD DE DATOS DEL VILLANO----------")
especieV = input("Escribe la especie del Villano: ")
nombreV = input("Escribe el nombre del Villano: ")
altV = float(input("Escribe la altura del Villano: "))
recargarV = int(input("Ingresa las balas del Villano: "))

#2. CREAR OBJETOS
Heroe = Personaje(especieH, nombreH, altH)
Villano = Personaje(especieV, nombreV, altV)

#3. USAR ATRIBUTOS
#4. USAR LOS METODOS
print("\n----------DATOS DEL HEROE----------")
print("El Heroe se llama: "+Heroe.nombre)
print("Pertenece a la especie: "+Heroe.especie)
print("Tiene una altura de: "+str(Heroe.altura))
Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargarH)

print("\n----------DATOS DEL VILLANO----------")
print("El Villano se llama: "+Villano.nombre)
print("Pertenece a la especie: "+Villano.especie)
print("Tiene una altura de: "+str(Villano.altura))
Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargarV)