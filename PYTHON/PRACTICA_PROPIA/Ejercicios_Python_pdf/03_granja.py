# En una granja hay V vacas, A aves(pollo,gallinas) y E escorpiones las vacas estan encerradas en un corral de K metros cuadrados, las aves en un galpon y los escorpiones en vitrinas.

# 1: Si una vaca necesita K metros cuadrados de pasto para producir X litros de leche por dia ¿cuantos litros de leche se producen por semana en la granja?.

def leche_producida(metros,semanas,vacas):
    
    operacion = semanas * 7
    
    if metros >= 100:
        
        lt_por_vaca = 100
        produccion_total = lt_por_vaca * operacion * vacas
        return produccion_total
        
    else:
        
        lt_por_vaca = 50
        produccion_total = lt_por_vaca * operacion * vacas
        return produccion_total


metros_de_pasto = 50
semanas = 2
vacas = 1

print(f"en {semanas} semanas se producen {leche_producida(metros_de_pasto,semanas,vacas)} litros de leche")


# 2: Si 1/3 de las aves que hay en la granja son gallinas y la mitad de las gallinas ponen 1 huevo cada 3 dias y la otra mitad 1 huevo cada 5 dias ¿en un mes cuantos huevos producen 1 mes === 30 dias.

def produccion_de_huevos(aves,dias):
    
    cantidad_gallinas = round((1/3) * aves,0)
    
    productora_1_3_huevo = cantidad_gallinas/2
    productora_1_5_huevo = cantidad_gallinas/2
    
    contador_1 = 0
    for i in range(3,30+1,3):
        contador_1 += 1
    
    contador_2 = 0
    for i in range(5,30+1,5):
        contador_2 += 1
    return (contador_1 * productora_1_3_huevo) + (contador_2 * productora_1_5_huevo)

aves = 100
dias = 30

print(produccion_de_huevos(aves,dias))




# 3: Si los escorpiones de la granja se venden a china y hay escorpiones de tres diferentes tamaños pequeños (20gramos) medianos (30gramos) grandes(50gramos) cuantos kilos de escorpiones se pueden vender sin que decrezca la poblacion a menos de 2/3?


def carne_de_escorpion(Pe):
    
    # gramos unidad de escorpion
    
    escorpion_pequeño = 20
    escorpion_mediano = 30
    escorpion_grande = 50
    
    kilo_pequeño = (escorpion_pequeño * Pe) / 1000  #0.88
    kilo_mediano = (escorpion_mediano * Pe) / 1000  #1.32
    kilo_grande = (escorpion_grande * Pe) / 1000 # 2.2
    
    kilo_total = kilo_pequeño + kilo_grande + kilo_mediano
    
    return kilo_total
    
poblacion_total = 200
poblacion_maxima =round((2/3) * poblacion_total,0)
poblacion_por_escorpion = poblacion_maxima // 3

print(f"se pueden vender {carne_de_escorpion(poblacion_por_escorpion)} kilos de carne sin que la poblacion baje de {poblacion_maxima} de escorpiones")

