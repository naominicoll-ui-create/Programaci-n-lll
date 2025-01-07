"Calcular el Cuadrado"
def cuadrado(numero):
    return numero ** 2

# Ejemplo
try:
    num = float(input("Ingresa un número: "))
    resultado = cuadrado(num)
    print(f"El cuadrado de {num} es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")
