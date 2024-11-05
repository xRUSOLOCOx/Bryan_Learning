class Coche():
    
    def __init__(self):
        
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4
        self.enMarcha = False
    
    def arrancar(self,arrancamos):
        
        self.enMarcha = arrancamos
        
        if (self.enMarcha):
            
            chequeo = self.__chequeo()
            
            if chequeo:
                
                return ("el carro esta en marcha")
            
            else:
                
                return ("No puede arrancar hay un problema con el chequeo")
        
        else:
            return ("el carro esta detenido")
        
    def estado(self):
        
        print(f"El coche tiene {self.__ruedas} ruedas , un ancho de {self.anchoChasis} y un largo de chasis de {self.largoChasis}")

    def __chequeo(self):
        
        print("Realizando chequeo")
        
        self.gasolina = "Ok"
        self.aceite = "Failed"
        self.puertaCerrada = "Ok"
        
        if self.gasolina == "Ok" and self.aceite == "Ok" and self.puertaCerrada == "Ok":
            
            return True
        
        else:
            
            return False
        
        
miCoche = Coche()

print(miCoche.arrancar(True))


