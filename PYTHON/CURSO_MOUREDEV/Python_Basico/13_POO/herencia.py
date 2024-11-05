class Vehiculos():
    def __init__(self,modelo,marca):
        
        self.modelo = modelo
        self.marca = marca
        self.arranca = False
        self.acelera = False
        self.frena = False
        
    def arrancar(self):
        
        self.arranca = True
        
    def acelerar(self):
        self.acelera = True
        
    def frenar(self):
        self.frena = True
        
    def estado(self):
        print(f"Marca: {self.marca} \nModelo {self.modelo} \nArranca: {self.arranca} \nAcelera: {self.acelera} \nFrena: {self.frena}")
        
class Furgoneta(Vehiculos):
    
    def carga(self,cargar):
        self.cargando = cargar
        
        if self.cargando:
            return "La furgo esta cargada"
        else:
            return "La furgo no esta cargada"
        
        
class Velectricos:
    
    def __init__(self):
        
        self.autonomia = 100
        
    def cargar_energia(self):
        
        self.cargando = True
    
class Moto(Vehiculos):
    
    hcaballito = ""
    
    def caballito(self):
    
        self.hcaballito = "Voy haciendo el caballito"
    
    def estado(self):
    
        print(f"Marca: {self.marca} \nModelo {self.modelo} \nArranca: {self.arranca} \nAcelera: {self.acelera} \nFrena: {self.frena} \nCaballito: {self.hcaballito}")


moto = Moto("X-01","YAMAHA")

moto.caballito()

moto.estado()


furgo = Furgoneta("JBL","RENAULT")
furgo.estado()
print(furgo.carga(False))

class biciElectrica(Velectricos,Vehiculos):
    
    pass

mibici = biciElectrica()

print(isinstance(mibici,Vehiculos))