# Las cadenas se pueden indexar:
# El primer caracter de la cadena tiene indice 0 

nombre = "Bryan"
print(nombre[0])
print(nombre[4])

# Los indices pueden ser negativos para contar desde la derecha:

nombre = "Emilio"
print(nombre[-1])
print(nombre[-6])

# Las cadena se pueden extraer en subcadenas usando slicing:

cadena = "Python"
print(cadena[0:6]) # Subcadena "Eduard"
print(cadena[2:])
print(cadena[-1::-1])
print(cadena[-4::-1])
print(cadena[-2:-5:-1])
print(cadena[-1:-4:-1])


print(cadena[:2]+cadena[2:])