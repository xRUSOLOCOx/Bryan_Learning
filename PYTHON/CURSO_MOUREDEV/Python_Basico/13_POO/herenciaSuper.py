class Persona():
    def __init__(self, nombre,edad,lugar_residencia):
        
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
        
    def Descripcion(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad} Residencia: {self.lugar_residencia}")

class Empleado(Persona):
    
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        
        self.salario = salario
        self.antiguedad = antiguedad
        
    def Descripcion(self):
        
        super().Descripcion()
        
        print(f"Salario: {self.salario} Antiguedad: {self.antiguedad}")


persona1 = Empleado(130000,20,"Manuel",18,"Bogota")

persona1.Descripcion()

