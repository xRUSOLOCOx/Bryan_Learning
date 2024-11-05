### Funciones aplicadadas a los strings pueden o no recibir parametros:###


# Convertir una cadena en mayusculas:

cadena = "python"
print(f"la cadena es: {cadena.upper()}") 

# Convertir una cadena en minusculas:

cadena = "PYTHON"
print(f"la cadena es: {cadena.lower()}") 

# Convertir primer caracter en mayuscula:

cadena = "python"
print(f"la cadena es: {cadena.capitalize()}") 

# Convertir cada primer caracter en mayuscula:

cadena = "python language"
print(f"la cadena es: {cadena.title()}") 

# Contar ocurrencias de un caracter en una cadena:

cadena = "python language"
print(f"ocurrencias en la cadena xd: {cadena.count("thon")}")  # string.count(valor, inicio, fin)

# Comprobar si es numerico:

cadena = "32"
print(f"ocurrencias en la cadena: {cadena.isnumeric()}") 


# Remover espacios de una cadena:

cadena = "  python language  "
print(f"la cadena es:{cadena.strip()}") 

# Comprueba si una cadena empieza o termina con un caracter:

cadena = "Hola mundo"
print(f"la cadena es:{cadena.startswith("H")}") 
print(f"la cadena es:{cadena.endswith("o")}") 

# Reemplazar ocurrencias de una subcadena por otra:

cadena = "abeja"
nueva_cadena = cadena.replace("a","o")
print(nueva_cadena)


# # Dividir una cadena en una lista o unir en una lista en una cadena

# cadena = "python language"
# palabras = cadena.split()

# print(palabras)

# unir = " ".join(palabras)
# print(unir)


# Formatear cadena de texto:

mi_texto = "Hola me llamo {}"
print(mi_texto.format("Bryan"))

mi_texto = "Mi nombre es {nombre} y mi edad es {edad} mi color es {color}".format(nombre = "Bryan",edad = 18, color = "Azul")
print(mi_texto)

mi_texto = "Mi nombre es %s y mi edad es %i mi color es %s" %("Bryan",18,"Azul")
print(mi_texto)
# Verificar si todos los caracteres pertenecen al alfabeto:

mi_texto = "Hola que mas".replace(" ","")
print(mi_texto.isalpha())


