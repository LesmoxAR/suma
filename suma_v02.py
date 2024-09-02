def leer_datos():
    a = int(input("Introduce el primer sumando: "))
    b = int(input("Introduce el segundo sumando: "))
    return a,b
def calcular_suma(a, b):
    return  a + b

a,b=leer_datos()
print(f"La suma es: {calcular_suma(a,b)}")
