#PROGRAMA LISTA DE FICHA 2924759

ficha = [
    "Zapata niño","Adriana Torres", "Andres Ortiz", "Bryan Pardo", "Camilo Paez",
    "Cristhian Paez", "Daniel Botia", "David Vergara", "Elianell Flores",
    "Felipe Diaz", "Jeimy Zapata", "Johan Aguilar", "Johan Gutierrez",
    "Johana Fernandez", "Juan Salgado", "Juan Cristancho", "Julio Medina",
    "Karen Niño", "Kelly Vargas", "Kevin Rojas", "Martin Gonzalez",
    "Michael Sandoval", "Miguel Beltran", "Nicolas Herrera", "Nicolas Rodriguez",
    "Nicolas Ariza", "Pablo Valenzuela", "Pablo Escobar", "Samary Cardozo",
    "Tomas Vega", "Valerid Hortua",""]

# PRIMER EJERCICIO IKPRIMIR TODOS LOS NOMBRES:

def imprimir_todo(lista):
    for nombre in lista:
        print(nombre)
        
def imprimir_todo_una_linea(lista):
    acumular = ""
    for nombre in lista:
        acumular += nombre + ","
    print(acumular)

# 2 EJERCICIO BUSCAR UN NOMBRE:

# def buscar(lista,buscar):

#     if buscar in lista:
#         ubicacion = lista.index(buscar)
#         print("El nombre %s si existe y esta en la pocicion %d" %(buscar,ubicacion))
#     else:
#         print("El nombre no existe")

# buscar(ficha,input("Buscar: "))

# 3 EJERCICIO AGREGAR NOMBRE:

# def agregar(lista,nombre):
    
#     lista.append(nombre)
#     print(f"el nombre {nombre} se agrego correctamente")
#     print(lista)
    
# agregar(ficha,input("Que nombre desea agregar: "))

# 4 ORDENAR LISTA Y REVERSA:

def ordenar(lista):
    
    lista.sort()
    print(lista)
    
ordenar(ficha)

def reversa(lista):
    lista.sort(reverse = True)
    print(lista)
    
reversa(ficha)