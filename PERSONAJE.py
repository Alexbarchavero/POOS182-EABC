class Personaje:
    
    #definir atributos
    especie = "Humano"
    nombre = "MasterChief"
    altura = 2.70
    
    #definir metodos
    def correr(self,status):
        if(status):
            print("El personaje "+self.nombre+" esta corriendo")
        else:
            print("El personaje "+self.nombre+" se detuvo")
    
    def lanzarGranadas(self):
        print("El personaje "+self.nombre+"lanzo la granada")
    
    def recargarArma(self,municiones):
        cargador = 10
        cargador += municiones
        print("El arma recargada tiene "+cargador+" balas")