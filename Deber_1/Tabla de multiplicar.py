"Tabla de multiplicar"
# Solicitar un número al usuario
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

# Mostrar la tabla de multiplicar del 1 al 10
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
