# En python existen distintas operaciones para manipular una cadena de caracteres
# Strings.

# Asignacion:

print("Asignacion:")

nombre = "Hola"
nombre += " "
nombre += "Bryan"

print(nombre)

#Concatenacion:

print("Concatenacion:")

saludo = "Hola"
espacio = " "
nombre =  "Bryan"

print(saludo + espacio + nombre)

numero_uno = 465
numero_dos = 6

resultado = numero_uno + numero_dos
resultado = str(resultado)

print("El resultado de la suma es: " + resultado)

#Busqueda:

print("Busqueda:")

nombre = "Bryan Pardo"
buscar_subcadena = nombre.find("Pardo")

print(buscar_subcadena)

#Extraccion:

print("Extraccion:")

mensaje = "Hola Bryan"
extraer_cadena = mensaje[0:5]

print(extraer_cadena)

#Comparacion:

print("Comparacion:")

mensaje_uno = "Hola"
mensaje_dos = "Hola"

comparacion = mensaje_uno == mensaje_dos
print(comparacion)
