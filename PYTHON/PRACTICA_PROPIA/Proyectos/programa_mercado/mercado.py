def validacion_opcion():

    # FUNCION PARA VALIDAR OPCION DE MENU:
    
    while True:

        opcion = input("Seleccion de opcion: ")  
            
        if opcion.isalpha():                  
            print("Error: Solo numeros permitidos") 
        elif opcion not in ["1","2","3","4"]: # LISTA DE VALORES PERIMITIDOS
            print("Error: opcion invalida")
        else:
            return opcion

def separador_visual():
    
    caracter = "-" * 40
    print(caracter)

# INICIALIZACION DE LISTAS:

producto = [] 
precios = []
longitud_principal = []

# CICLO DE FUNCIONAMIENTO PRINCIPAL:

while True:

    # MENU DE OPCIONES:
    
    separador_visual()
    
    print("""seleccione una opcion:

    1: Registrar producto
    2: Registar precios de producto
    3: eliminar producto
    4: cambiar precio
    4: Salir""")
    
    separador_visual()
    

    # OPCION 1 REGISTRO DE PRODUCTOS:
    
    match validacion_opcion():
        
        
        case "1":
        
            registro_de_productos = input("Ingrese alimentos: ")
            separar_registro = registro_de_productos.split(" ")
            filtrar_lista = list(filter(None,separar_registro))
                
            producto.extend(filtrar_lista)
            print(f"los productos {producto} han sido registrados")
            
            longitud_principal.append(str(len(producto)))
            
            longitud = []
            longitud.append(str(len(producto)))
            print(longitud)
            print(longitud_principal)

        case "2":
        
            valor = longitud_principal[0]
            nueva_lista = list((valor))

            
            if len(producto) == 0:
                
                print("No hay productos registrados")
                
            elif len(producto) == len(precios):
                print("Ya registro los producto")
                
            elif nueva_lista == longitud:
                
                    print(f"Los productos registrados son: {producto}")
                    for alimento in producto:
                        registro_precio = input(f"{alimento}:$")
                        precios.append(registro_precio)
                            

            else: 
                    convertir = int(longitud_principal[0])
                    extraer_nuevo = producto[convertir:]
                    
                    print(f"los nuevos productos registrados:{extraer_nuevo}")
                    for alimento in extraer_nuevo:
                        registro_precio = input(f"{alimento}:$")
                        precios.append(registro_precio)
                        
                    nueva_longitud_principal = len(extraer_nuevo) + convertir
                    
                    longitud_principal.insert(0,nueva_longitud_principal)
                    print(extraer_nuevo)
                    print(precios)


        case "3":

        
            if len(producto) == 0:
                print("No hay productos registrados")

            else:
                print(f"Los productos registrados son: {producto}")
                seleccion_producto_eliminar = input("Seleccione el producto a eliminar: ")
                
                if seleccion_producto_eliminar not in producto:
                    print("El producto no esta registrado")
                else:
                    producto.remove(seleccion_producto_eliminar)
                    
                    print(f"Los productos registrados son: {producto}")


        case "4":
        
            if len(producto) == 0 or len(precios) == 0:
                print("No hay productos o precios registrados")
                
            else:
                
                for elemento1, elemento2 in zip(producto,precios):
                    mensaje = (f"{elemento1}: {elemento2}")   
                    print(mensaje)
            
                seleccion_cambio_producto = input("Seleccione el producto al que desea cambiar el precio: ")
                cambio_precio = input(f"ingrese el nuevo precio de:{seleccion_cambio_producto}:$")
                cambio_precio = int(cambio_precio)
            
                indice_de_producto = producto.index(seleccion_cambio_producto)
                precios.pop(indice_de_producto)
                
                #AGREGAR NUEVO PRECIO A LA LISTA:
                
                precios.insert(indice_de_producto,cambio_precio)
                print(precios)
                


