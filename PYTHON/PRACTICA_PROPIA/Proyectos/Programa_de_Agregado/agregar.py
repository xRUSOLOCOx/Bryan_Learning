def agregar(lista):
    while True:
        agregar = input("Agrege un nombre: ")
        
        if agregar in lista:
            print("El nombre ya esta")
        else:
            lista.append(agregar)
            print(lista)
            break


def eliminar(lista):
    while True:
        
        eliminar = input("Elimine un nombre: ")
        
        if eliminar not in lista:
            print("El nombre ya esta eliminado")
        else:
            lista.remove(eliminar)
            print(lista)
            break

nombres = []
print(nombres)

while True:
    
    opcion = input("Desea eliminar o agregar elemento (E O A): ").upper()
    
    if opcion == "ELIMINAR" or opcion == "E":
        eliminar(nombres)
    elif opcion == "AGREGAR" or opcion == "A":
        agregar(nombres)
        
    parada = input("Desea continuar (S/N)").upper()
    if parada == "N":
        break