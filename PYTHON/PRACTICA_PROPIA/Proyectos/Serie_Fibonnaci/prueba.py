# Serie de Fibonacci

a = 0
b = 1
resultado = [a]  # Inicia la lista con el primer número de la serie

for _ in range(19):  # Solo necesitas 19 iteraciones porque el primer número ya está en la lista
    c = a + b
    resultado.append(c)  # Agrega el nuevo número al final de la lista
    a = b
    b = c
print(resultado)
print(f"La serie de Fibonacci es {' '.join(map(str, resultado))}")
