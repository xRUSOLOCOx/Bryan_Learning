# Si en la UN estan podando arboles y cada rama tiene 20 hojas y a cada arbol le quitaron 100 ramas cuantos arboles de deben podar para obtener 50000 hojas?

def podar_arbol(objetivo,ramas,cantidad_arboles):
    
    hoja_por_rama = 20
    hojas_totales = ramas * hoja_por_rama
    
    for i in range(1,cantidad_arboles+1):
        
        operacion = hojas_totales * i
        
        if operacion >= objetivo:
            arboles = i
            return arboles
        
    return -1


objetivo_hojas = 15000 # ramas a obtener
cantidad_de_ramas = 100 # promedio ramas de acacia
cantidad_de_arboles = 50 # cantidad de arboles disponibles


print(f"para obtener {objetivo_hojas} ramas se deben podar: {podar_arbol(objetivo_hojas,cantidad_de_ramas,cantidad_de_arboles)} arboles")




