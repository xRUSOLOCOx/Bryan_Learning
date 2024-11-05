### CLASES ###


class PersonaVacia:
    pass


class Persona:
    
    def __init__(self,nombre,apellido):
        
        self.nombre = nombre
        self.__apellido = apellido
        self.edad = 18
        
    def walk(self):
        print(f"{self.nombre} esta caminando")
        
    
myperson = Persona("Bryan","Pardo")


print(myperson.edad)

myperson.__apellido = "bicho"
print(myperson.__apellido)





