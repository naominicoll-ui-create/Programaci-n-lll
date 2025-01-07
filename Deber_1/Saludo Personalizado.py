"Saludo Personalizado"
def saludar(nombre):
    return f"¡Hola {nombre}, Como estas? ! Que tengas un muy bonito dia hoy."
# Ejemplo
nombre_usuario = input("Ingresa tu nombre: ")
saludo = saludar(nombre_usuario)
print(saludo)