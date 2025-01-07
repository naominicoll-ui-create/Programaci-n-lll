"Calculadora"
# Solicitar dos números y la operación
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

# Realizar el cálculo según la operación ingresada
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: No se puede dividir entre cero."
else:
    resultado = "Operación no válida."

# Mostrar el resultado
print(f"El resultado es: {resultado}")
