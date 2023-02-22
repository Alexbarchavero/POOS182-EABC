class Personaje:
    
    # Constructor
    def __init__(self,esp,name,alt):
        self.especie = esp
        self.nombre = name
        self.altura = alt
    
    #definir metodos
    def correr(self,status):
        if(status):
            print("El personaje "+self.nombre+" esta corriendo")
        else:
            print("El personaje "+self.nombre+" se detuvo")
    
    def lanzarGranadas(self):
        print("El personaje "+self.nombre+" lanzo la granada")
    
    def recargarArma(self,municiones):
        cargador = 10
        cargador += municiones
        print(f"El arma recargada tiene {cargador} balas")