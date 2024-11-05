"""Login de usuario basico"""

usuarios = {}
def correo_fun():
    while True:
        correo = input("Ingrese su correo: ")
        
        if correo.count("@") != 1:
            print("Error: correo invalido")
        elif correo[0] == "@" or correo[-1] == "@":
            print("Error: correo invalido")
        elif correo.count(".") != 1:
            print("Error: correo invalido")
        else:
            print(f"{correo} correo valido registrado")
            return correo

def minuscula(cadena):
    for caracter in cadena:
        if caracter.islower():
            return True
def mayuscula(cadena):
    for caracter in cadena:
        if caracter.isupper():
            return True
def digito(cadena):        
    for caracter in cadena:
        if caracter.isdigit():
            return True    
        
    
def contraseña_fun():
    
    print("""Ingrese su contraseña
    8 caracteres que contegan una mayuscula,
    un digito y una minuscula (como minimo):              
    """)
    
    while True:
        contraseña = input("Contraseña: ")
        
        if minuscula(contraseña) != True:
            print("contraseña invalida")
        elif mayuscula(contraseña) != True:
            print("contraseña invalida")
        elif digito(contraseña) != True:
            print("contraseña invalida")
            
        else:
            print(f"{contraseña} es valida")
            return contraseña
        
def registrar_usuario():
    correo = correo_fun()
    contraseña = contraseña_fun()
    usuarios[correo] = contraseña
    print("Usuario registrado con éxito.")


print("""Bienvenido al sistema

opcion 1: Registrarse
opcion 2: Login
    """)


while True:

    opcion = input("Opcion solo numero: ")
    
    if opcion.isnumeric() == False:
        print("Error: solo numeros")
        
    elif opcion != "1" and opcion != "2":
        print("Error: opcion invalida")
        
    elif opcion == "1":
        registrar_usuario()
        break

print(usuarios)


