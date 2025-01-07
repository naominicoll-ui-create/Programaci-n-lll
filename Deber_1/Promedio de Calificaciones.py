"Promedio de Calificaciones"
def calcular_promedio():
    calificaciones = []
    while True:
        try:
            calificacion = float(input("Ingresa una calificación (o -1 para terminar): "))
            if calificacion == -1:
                break
            elif 0 <= calificacion <= 10:
                calificaciones.append(calificacion)
            else:
                print("Por favor, ingresa una calificación válida entre 0 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio de las calificaciones es: {promedio:.2f}")
    else:
        print("No se ingresaron calificaciones para calcular el promedio.")
