### Manejo de Excepciones ###

numero_uno = 5
numero_dos = "1"

try:
    
    print(numero_uno + numero_dos)

except:
    print("Error detectado")
    
else:
    print("operacion satisfactoria")
    
finally:
    print("tenga un buen dia")
    
    
    
# Excepciones por tipo.
try:
    
    print(numero_uno + numero_dos)

except TypeError:
    
    print("Error detectado")

# Captura de la excepcion:

try:
    
    print(numero_uno + numero_dos)

except TypeError as error:
    
    print("Error detectado")
    


# def incremento(total):
    
#     razon = (total * 0.02)/1
#     dinero_total = f"Su ingreso inicial es ${total} con porcentaje de 2% su incremento total en un mes es {total+razon}"
    
#     return dinero_total

# dinero = float(input("Ingrese su total $"))
# print(incremento(dinero))

# def comisiones(sueldo,ventas):
    
#     comision = (ventas * 0.1)/1
#     sueldo_total = f"sueldo base {sueldo} recibe de comison por {ventas}  y el total del sueldo es {sueldo + comision}"
    
#     return sueldo_total

# sueldo_base = float(input("Ingrese su sueldo base: "))

# v1 = float(input("Ingrese valor venta 1: "))
# v2 = float(input("Ingrese valor venta 2: "))
# v3 = float(input("Ingrese valor venta 3: "))

# print(comisiones(sueldo_base,v1+v2+v3))

numero = int(input("Tabla del: "))
for i in range(1,11):
    operacion = numero * i
    print(f"{numero} X {i} = {operacion}")
