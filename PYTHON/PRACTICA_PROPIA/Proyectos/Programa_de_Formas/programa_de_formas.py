import turtle

# creando funciones de movimiento basico

def adelante(longitud):
    mover= turtle.forward(longitud)


def atras(longirud):
    mover = turtle.backward(longirud)


def girar_derecha(grados):

    girar = turtle.right(grados)


def girar_izquierda(grados):
    girar = turtle.left(grados)


def lapiz_arriba():
    levlapiz = turtle.penup()


def lapiz_abajo():
    bajlapiz = turtle.pendown()


def newplace(x,y):
    lapiz_arriba()
    newplace = turtle.goto(x,y)
    lapiz_abajo()



"""------------------------------------------------------------------------------------------------------"""

def cuadrado(longitud_lado):
    for lado in range(4):
        adelante(longitud_lado)
        girar_izquierda(90)
        
def triangulo(longitud_lado):
    for lado in range(3):
        adelante(longitud_lado)
        girar_izquierda(120)
        
def rectangulo(lado_mayor,lado_menor):
    for lado in range(2):
        adelante(lado_mayor)
        girar_izquierda(90)
        adelante(lado_menor)
        girar_izquierda(90)

# Configuracion de la ventana de turtle

# ventaja = turtle.Screen()
# ventaja.bgcolor("white")
# ventaja.title("Creando Figuras")


print("""
Bienvenido a la creacion de figuras:

selecciona una de las formas disponibles:
cuadrado, circulo, triangulo, rectangulo.
""")

seleccion = str(input("Forma: ")).capitalize()

if seleccion == "Cuadrado" or seleccion == "C":
    longitud_lado = int(input("Longitud de lado cuadrado: "))
    newplace(0,-250)
    cuadrado(longitud_lado)
    turtle.done()
elif seleccion == "Triangulo" or seleccion == "T":
    longitud_lado = int(input("Longitud de lado triangulo: "))
    newplace(0,-250)
    triangulo(longitud_lado)
    turtle.done()
elif seleccion == "Rectangulo" or seleccion == "R":
    longitud_lado_mayor = int(input("Longitud de lado mayor del Rectangulo: "))
    longitud_lado_menor = int(input("Longitud de lado menor del Rectangulo: "))
    newplace(0,-250)
    rectangulo(longitud_lado_mayor,longitud_lado_menor)
    turtle.done()
    
    turtle.width