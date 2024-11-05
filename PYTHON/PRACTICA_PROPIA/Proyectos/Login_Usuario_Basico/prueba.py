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
            return correo + "hola"
        
print(correo_fun())








        # print(f"correo:{correo_fun()} registrado")
        # print(f"contraseña:{contraseña_fun()} registrado")