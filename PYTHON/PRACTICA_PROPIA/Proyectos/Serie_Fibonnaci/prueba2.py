lista = []

cadena = "arroz pollo".replace(" ","")

for letra in cadena:  
    lista.append(letra)
print(lista)

cadena = ""
for letra in lista:   
    cadena += letra
print(cadena[:5] + " " + cadena[5:])

