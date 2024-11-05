# Diccionario: Estructura de datos de relacion clave : valor


mi_diccioanrio = dict()
mi_otro_diccionario = {}

print(type(mi_diccioanrio))
print(type(mi_otro_diccionario))

mi_diccioanrio = {"Nombre":"Bryan","Apellido":"Pardo","Edad":18}

mi_otro_diccionario ={
    
    "Color":"Azul",
    "Idiomas":["Ingles","Español"],
    "Deporte":"Futbol",
    "Lenguajes":{"Python","JS","Java"}
    
}


print(mi_diccioanrio)
print(mi_otro_diccionario)


# Definir nueva clave:

mi_otro_diccionario["Color"] = "Negro"
print(mi_otro_diccionario)

# Acceder a una clave:

print(mi_diccioanrio["Nombre"])
print(mi_diccioanrio["Edad"])

print(mi_otro_diccionario.pop("Color"))


print("Bryan" in mi_diccioanrio)
print("Bryan" in mi_diccioanrio.values())

print(mi_otro_diccionario.items())
print(mi_otro_diccionario.keys())
print(mi_otro_diccionario.values())

mi_lista = ["nombre","apellido","edad",1,43]

# Diccionario con claves pero sin valores:

print(dict.fromkeys(mi_lista))
print(dict.fromkeys(["queso","comida"]))

nombres = ["Alice", "Bob", "Charlie"]

for i in range(len(nombres)):
    nombres[i] = nombres[i].upper()  # Convierte cada nombre a mayúsculas

print(nombres)



hola = {"Name":18}
chao = {"Name2":19}

print(hola | chao)