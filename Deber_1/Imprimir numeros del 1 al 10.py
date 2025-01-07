"Imprimir numeros del 1 al 10"
# Usar un bucle para mostrar los números del 1 al 10 en una sola línea
for numero in range(1, 11):
    if numero < 10:
        print(numero, end=", ")
    else:
        print(numero)
