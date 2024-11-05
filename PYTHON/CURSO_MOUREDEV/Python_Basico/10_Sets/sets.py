### Sets ###

# Los sets son unos de los 4 tipos de datos incorporados de Python usados para almacenar arreglos de datos. Un set tiene caracteriscas unicas como que es desordenado, no indexado, incambiable y no admite duplicados.

frutas_set = {"Manzana","Pera","Melon"}
print(frutas_set) # Lo imprime de forma desordenada

# Set con distintos tipos de datos:

frutas_set = {"Manzana","Pera","Melon"}
edades = {18,22,50,80}
precios = {1.000,50.000,1.00000}
booleanos = {True,False,True,False}

# Set anidado:

mi_set = {"Manzana",18,2.5,True}
print(type(mi_set))

# Constructor de SET set():

frutas_set = set(("Manzana","Pera","Melon"))
print(frutas_set)


# No se pueden acceder a los elementos de un set con su indice, La unica forma es un for loop.

for item in frutas_set:
    print(item)


#----------------------------------------------------------------------------------------------------------#

# Metodos Set:


# Añadir elementos al Set:

frutas_set = {"Manzanam","Pera","Melon"}
frutas_set.add("Fresa")


print(frutas_set)

# Remover elementos al Set:

frutas_set = {"Manzana","Pera","Melon","Fresa"}
frutas_set.remove("Fresa")

print(frutas_set)

# Actualizar un Set:

frutas_set = {"Manzana","Pera","Melon","Fresa"}
vegetales_set = {"Cebolla","Tomate","Brocoli"}

frutas_set.update(vegetales_set)
frutas_set.update({"Coliflor"})

print(frutas_set)

# Remover elementos de un Set:

colores_set = {"Amarillo","Azul","Rojo"}
colores_set.remove("Amarillo")
print(colores_set)

colores_set.discard("Verde")

# Limpiar Set:

colores_set.clear()

# Unir Sets Union admite iterables de cualquier tipo:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set5 = set1.union(set2,set3,set4)
set6 = set1 | set2 | set3 | set4

print(set5)
print(set6)

# Nuevo Set que retorna los duplicados entre dos Sets:

frutas = {"apple", "banana", "cherry"}
sistemas = {"google", "microsoft", "apple","cherry"}

print(frutas.intersection(sistemas))
print(frutas & sistemas)