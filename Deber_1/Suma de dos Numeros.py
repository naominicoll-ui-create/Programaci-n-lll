"Suma de dos Numeros"
def sumar(numero1, numero2):
    return numero1 + numero2

# Ejemplo
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = sumar(num1, num2)
    print(f"La suma de {num1} y {num2} es: {resultado}")
except ValueError:
    print("Por favor, ingresa valores numéricos válidos.")
