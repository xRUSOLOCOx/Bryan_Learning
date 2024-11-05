def validacion_opcion():

    # FUNCION PARA VALIDAR OPCION DE MENU:
    
    while True:

        opcion = input("Seleccion de opcion: ")  
            
        if opcion.isalpha():                  
            print("Error: Solo numeros permitidos") 
        elif opcion not in ["1","2","3","4","5","6"]: # LISTA DE VALORES PERIMITIDOS
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
    
    print(""" Bienvenido al sistema , seleccione una opcion:

    1: Registrar producto
    2: Registar precios de producto
    3: eliminar producto
    4: cambiar precio
    5: Realizar venta
    6: Salir del sistema""")
    
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


            validaciones = ""
            match validaciones:
                
                case x if len(producto) == 0:
                
                
                    print("No hay productos registrados")
                    
                case x if len(producto) == len(precios):
                
                    print("Ya registraron los producto")
                    
                case x if nueva_lista == longitud:
                
                    print(f"Los productos registrados son: {producto}")
                    for alimento in producto:
                        registro_precio = input(f"{alimento}:$")
                        precios.append(registro_precio)
                            
                case x:
                    
                    convertir = int(longitud_principal[0])
                    extraer_nuevo = producto[convertir:]
                        
                    print(f"los nuevos productos registrados:{extraer_nuevo}")
                    for alimento in extraer_nuevo:
                        registro_precio = input(f"{alimento}:$")
                        precios.append(registro_precio)
                            
                        nueva_longitud_principal = str(len(extraer_nuevo) + convertir)
                        
                        longitud_principal.insert(0,nueva_longitud_principal)


        case "3":
            
            validaciones = ""
            match validaciones:
                
                case x if len(producto) == 0:

                    print("No hay productos registrados")

                case x:
                    print(f"Los productos registrados son: {producto}")
                    seleccion_producto_eliminar = input("Seleccione el producto a eliminar: ")
                
                    if seleccion_producto_eliminar not in producto:
                        print("El producto no esta registrado")
                    else:
                        indice_de_precio = producto.index(seleccion_producto_eliminar)
                        producto.remove(seleccion_producto_eliminar)
                        precios.pop(indice_de_precio)
                    print(f"Los productos registrados son: {producto}")
                    print(precios)


        case "4":
            
            validaciones = ""
            match validaciones:
                
                case x if (producto) == 0 or len(precios) == 0:
                    print("No hay productos o precios registrados")

                
                case x:
                
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
                    
        case "5":
            
            if len(producto) != len(precios):
                print("Producto sin precio")
                
            else:    
                cantidades = []
                pago_total = 0
                print(f"Los producto registrados son: {producto}")
                print(f"Los precios registrados son:  {precios}")
                

                seleccion_producto_venta = input(f"escriba los productos a comprar separados por espacio: ")
                seleccion_producto_venta = seleccion_producto_venta.split(" ")
                
                for alimento in seleccion_producto_venta:
                    cantidad = input(f"{alimento} Cantidad: ")
                    
                    if cantidad.isalpha():
                        print("Error la cantidad no puede ser una letra")
                    else:
                        cantidad = int(cantidad)
                        cantidades.append(cantidad)


                for alimento,cantidad in zip(seleccion_producto_venta,cantidades):
                    
                    ind = producto.index(alimento)
                    precio = precios[ind]
                    
                    print(f"{alimento}:${precio} {cantidad}")
                    operacion = int(precio) * cantidad

                    pago_total += operacion
                print(f"precio total es: {pago_total}")
                