# Strings(Cadena de texto):

'Hola mundo' # Comillas 

"Bienvenido al curso de python" # Comillas dobles

"12345" # Numeros entre comillas son strings


# Secuencias de escape citar una cita con \ y comillas:

"Hola, 'mundo'"
'"Si," me gusta'
"Ellos son \"amigos\""

# Salto de linea:

texto = 'Primera linea. \nSegunda linea.'
print(texto)

print("""
nombre =
apellido = 
      """)

# Formateo de strings:

nombre, apellido, edad = "Bryan", "Pardo", 18

print("Mi nombre es:{} {} y mi edad es: {}" .format(nombre,apellido,edad))
print("Mi nombre es:%s %s y mi edad es: %d" %(nombre,apellido,edad))
print(f"Mi nombre es: {nombre} {apellido} y mi edad es: {edad} ")


# Desempaquetado de strings:

language = "Python"

a,b,c,d,e,f = language

print(a)
print(b)
print(c)
print(d)

