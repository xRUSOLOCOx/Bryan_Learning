mis_datos = [1.75,18,"Pardo","Bryan","Azul",18]

if len(mis_datos) == len(set(mis_datos)):
    
    print("no hay repetidos")
    
else:
    
    print("hay repetidos")
    print("aqui esta la lista sin repetidos:",list(set(mis_datos)))
    