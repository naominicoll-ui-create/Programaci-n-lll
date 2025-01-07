"Sistema de Calificaciones"
# Solicitar la calificación numérica
calificacion = float(input("Ingresa tu calificación (0-100): "))

# Determinar la letra correspondiente
if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion <= 89:
    letra = "B"
elif 70 <= calificacion <= 79:
    letra = "C"
elif 60 <= calificacion <= 69:
    letra = "D"
else:
    letra = "F"

# Mostrar la letra correspondiente
print(f"Tu calificación es: {letra}")
