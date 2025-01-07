"Clasificacion de Edades"
# Solicitar la edad del usuario
edad = int(input("Ingresa tu edad: "))

# Clasificar según la edad
if edad >= 0 and edad <= 12:
    clasificacion = "niño"
elif edad >= 13 and edad <= 17:
    clasificacion = "adolescente"
else:
    clasificacion = "adulto"

# Mostrar la clasificación
print(f"Eres un {clasificacion}.")
