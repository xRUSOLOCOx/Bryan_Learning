ficha = [
    "Adriana Torres", "Andres Ortiz", "Bryan Pardo", "Camilo Paez",
    "Cristhian Paez", "Daniel Botia", "David Vergara", "Elianell Flores",
    "Felipe Diaz", "Jeimy Zapata", "Johan Aguilar", "Johan Gutierrez",
    "Johana Fernandez", "Juan Salgado", "Juan Cristancho", "Julio Medina",
    "Karen Niño", "Kelly Vargas", "Kevin Rojas", "Martin Gonzalez",
    "Michael Sandoval", "Miguel Beltran", "Nicolas Herrera", "Nicolas Rodriguez",
    "Nicolas Ariza", "Pablo Valenzuela", "Pablo Escobar", "Samary Cardozo",
    "Tomas Vega", "Valerid Hortua"
]

def filtrar_bucle(lista):
    letra = "B"
    nombres_filtrados = []
    for elemento in lista:
        if elemento.startswith(letra):
            nombres_filtrados.append(elemento)
    return nombres_filtrados

def filtrar_comprension(lista):
    letra = "B"
    return [elemento for elemento in lista if elemento.startswith(letra)]

import timeit

# Medir el tiempo de ejecución del bucle `for`
tiempo_bucle = timeit.timeit(lambda: filtrar_bucle(ficha), number=10000)

# Medir el tiempo de ejecución de la comprensión de listas
tiempo_comprension = timeit.timeit(lambda: filtrar_comprension(ficha), number=10000)

tiempo_bucle, tiempo_comprension
