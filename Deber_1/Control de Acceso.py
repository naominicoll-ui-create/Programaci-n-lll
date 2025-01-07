"Control de Acceso"
# Definir el nombre de usuario y la contraseña correctos
usuario_correcto = "Noah2030"
contraseña_correcta = "Nicolas123"

# Establecer el número de intentos permitidos
intentos = 3

# Iniciar el ciclo para permitir los intentos
while intentos > 0:
    # Solicitar el nombre de usuario y la contraseña
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")

    # Validar si el nombre de usuario y la contraseña son correctos
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("¡Acceso permitido!")
        break  # Salir del ciclo si el acceso es correcto
    else:
        intentos -= 1  # Restar un intento si la combinación es incorrecta
        if intentos > 0:
            print(f"Nombre de usuario o contraseña incorrectos. Te quedan {intentos} intentos.")
        else:
            print("Acceso bloqueado. Has agotado todos los intentos.")
