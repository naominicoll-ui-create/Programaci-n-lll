"Juego de Numeros"
import random

def adivina_numero():
    numero_aleatorio = random.randint(1, 10)
    try:
        adivinanza = int(input("Adivina el número entre 1 y 10: "))
        if adivinanza == numero_aleatorio:
            print("¡Felicidades, acertaste!")
        else:
            print("Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
