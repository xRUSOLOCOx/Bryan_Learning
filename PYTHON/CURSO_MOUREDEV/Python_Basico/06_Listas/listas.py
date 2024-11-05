##3 Estructura con elementos ordenados y de todos los tipos ###

# Crear una lista:

mi_lista = list() # Listas vacias
mi_otra_lista = []

mi_lista = list((44,54,32,76,17,28)) # Listas con elementos
mi_otra_lista = [44,54,32,76,17,28]


# operaciones con listas:

mi_lista = [18,"Bryan","Pardo",1.75] # Lista con ekementos de distintos tipos

print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[3])

print(mi_lista[-1])
print(mi_lista[0:3])
print(mi_lista[1+2])
print(mi_lista.count("Bryan"))

# Desempaquetado de lista:

edad, nombre, apellido, medida = mi_lista

print(edad)
print(nombre)

# Reemplazar elemento de un lista:

mi_lista = [18,"Bryan","Pardo",1.75]

mi_lista[0] = 19
print(mi_lista)


