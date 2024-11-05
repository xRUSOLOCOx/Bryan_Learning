# Serie de fibonacci:

a = 0
b = 1
print(0)
resultado = ""

for i in range(19):
    
    c = a + b
    resultado += str(c) + " "
    b = a
    a = c
    
print(f"la serie de fibonacci es 0 {resultado}")

