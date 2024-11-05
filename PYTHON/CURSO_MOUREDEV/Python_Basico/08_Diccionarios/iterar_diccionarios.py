def ingresar_datos(id,N,A,E,D):
    
    registro = {id:{"Nombre":N,"Apellido":A,"Edad":E,"Deporte":D}}
    
    return registro



usuarios = {}
numero_usuario = 0

while True:
    
    salida = input("Desea salir S/N")
    
    if salida == "S" or salida == "s":
        break
    
    else:
        
        print(f"este es el diccionario de usuarios: {usuarios}")
        
        numero_usuario += 1
        nombre = input("Ingrese nombre")
        apellido = input("Ingrese apellido")
        edad = input("Ingrese edad")
        deporte = input("Ingrese deporte favorito")
        
        registro = ingresar_datos(numero_usuario,nombre,apellido,edad,deporte)
        
            
        usuarios |= registro
        print(usuarios)