# la Compresion de listas permite crear una nueva
# a partir de iteraciones en una sola linea:


# Extraer las frutas que empiezen por M:

lista = list(("Manzana","Mango","Pera","Uva","Melon","Naranga"))
nueva_lista = []

for fruta in lista:
    if fruta[0] == "M":
        nueva_lista.append(fruta)
print(nueva_lista)

nueva_list = [fruta for fruta in lista if fruta[0] == "M"]
print(nueva_list)


# Crear una lista de los primeros 10 números elevados al cuadrado:

elevados = [numero ** 2 for numero in range(1,11)]
print(elevados)

# Filtrar los números pares de una lista de números del 1 al 20.

pares = [numero for numero in range(1,21) if numero % 2 == 0]
print(pares)

