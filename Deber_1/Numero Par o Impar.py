"Numero Par o Impar"
def es_par(numero):
    return numero % 2 == 0

# Ejemplo
try:
    num = int(input("Ingresa un número: "))
    if es_par(num):
        print(f"{num} True.")
    else:
        print(f"{num} False.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
