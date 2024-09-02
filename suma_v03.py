class operaciones_aritmeticas():
    def leer_datos():
        a = int(input("Introduce el primer sumando: "))
        b = int(input("Introduce el segundo sumando: "))
        return a, b

    def calcular_suma(a, b):
        return a + b


operacion = operaciones_aritmeticas
a, b = operacion.leer_datos()
print(f"La suma es: {operacion.calcular_suma(a, b)}")
