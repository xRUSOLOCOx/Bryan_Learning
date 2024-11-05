import turtle

def poligono(lados):
    
    angulo_de_inclinacion = 360 / lados
    
    for i in range(lados):
        
        turtle.forward(40)
        turtle.left(angulo_de_inclinacion)


print("""Bienvendo a la creacion de poligonos:

Selecciones uno de los poligonos disponibles:

triangulo: 3 lados
cuadrado: 4 lados
pentagono: 5 lados
exagono: 6 lados
septagono: 7 lados
octagono: 8 lados
nonagono: 9 lados
decagono: 10 lados

""")
lados = input("Ingrese la cantidad de lados del poligono")
lados = int(lados)

if lados > 10:
    print(f"{lados} excede el limite valido")
else:
    lados = int(lados)
    poligono(lados)
    turtle.done()
    

