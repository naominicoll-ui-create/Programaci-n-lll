"Invertir un numero"
def invertir_numero(numero):
    signo = -1 if numero < 0 else 1
    numero_invertido = int(str(abs(numero))[::-1])  # Convertir a cadena, invertir, y convertir de nuevo a entero
    return signo * numero_invertido

# Solicitar al usuario un número entero
try:
    numero = int(input("Ingresa un número entero: "))
    resultado = invertir_numero(numero)
    print(f"La versión invertida de {numero} es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
