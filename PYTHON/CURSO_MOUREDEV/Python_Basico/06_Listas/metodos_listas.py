### Funciones aplicadadas a las listas pueden o no recibir parametros:###


# Agregar elemento en la ultima posicion:

mi_lista = list((18,"Bryan","Pardo",1.75))
mi_lista.append(62)

# Agregar elemento en una posicion determinada:

mi_lista.insert(3,"Azul")

# Eliminar elemento determinado:

mi_lista.remove("Azul")
# Eliminar elemento determinado y lo devuelve:
mi_lista.pop(4)

#------------------------------------------------------------------------------------------------------#

mi_lista.append("Azul")
mi_lista.append("62")
print(mi_lista)

#------------------------------------------------------------------------------------------------------#

# Eliminar elemento determinado:

del mi_lista[4]
print(mi_lista)

# Elimiar todos los elementos de la lista:
# mi_lista.clear()
# print(mi_lista)

# Revertir orden de elementos:

mi_lista.reverse()
print(mi_lista)