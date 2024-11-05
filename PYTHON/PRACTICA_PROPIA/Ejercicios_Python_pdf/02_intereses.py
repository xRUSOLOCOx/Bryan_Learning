# Si un amigo no tan amigo me presta K pesos a i pesos de interes diario. Cuanto le pagare en una semana si el interes es simple y compuesto?.

def interes_simple(monto,interes,duracion):
    
    duracion_semanal = duracion/52
    porcentaje_interes = interes/100
    
    interes_simple = monto * porcentaje_interes * duracion_semanal
    
    return round(interes_simple,2)

def interes_compuesto(monto,interes,duracion,n):
    
    porcentaje_interes = interes/100
    duracion_semanal = duracion/52
    
    operacion1 = (porcentaje_interes / n) + 1
    nt = 1 * duracion_semanal
    operacion2 = operacion1 ** nt
    
    interes_compuesto = monto * operacion2
    
    return round(interes_compuesto,2)


print(interes_simple(3000000,5,52))

print(interes_compuesto(1000000,5,156,1))