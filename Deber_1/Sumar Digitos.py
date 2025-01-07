"Sumar Digitos"
def suma_digitos(numero):
    suma = 0
    for digito in str(abs(numero)):
        suma += int(digito)
    return suma

# Solicitar al usuario un número entero
try:
    numero = int(input("Ingresa un número entero: "))
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
