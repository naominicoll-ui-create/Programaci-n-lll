"Validar Contraseña"
# Definir la contraseña correcta
contraseña_correcta = "Noah2030"

# Solicitar la contraseña al usuario
contraseña = input("Ingresa la contraseña: ")

# Validar si la contraseña es correcta
if contraseña == contraseña_correcta:
    print("Contraseña correcta. Acceso permitido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")
