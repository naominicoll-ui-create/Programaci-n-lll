"Calcular el area de un circulo"
import math

def area_circulo(radio):
    return math.pi * radio ** 2

# Ejemplo
try:
    radio = float(input("Ingresa el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El área del círculo con radio {radio} es: {area:.2f}")
except ValueError:
    print("Por favor, ingresa un número válido para el radio.")
