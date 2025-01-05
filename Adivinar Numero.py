"Adivinar Numero"
import tkinter as tk
import random

import tkinter as tk
import random

# Variables del juego
def reiniciar_juego():
    global numero_secreto, intentos_restantes
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 10
    lbl_resultado.config(text="¡Comienza el juego! Intenta adivinar el número.", fg="#00FF00")
    lbl_intentos.config(text=f"Intentos restantes: {intentos_restantes}")
    entrada_numero.delete(0, tk.END)
    btn_adivinar.config(state=tk.NORMAL)  # Habilitar el botón para adivinar

def verificar_intento():
    global intentos_restantes
    intento = entrada_numero.get()

    if not intento.isdigit():
        lbl_resultado.config(text="Por favor, ingresa un número válido.", fg="red")
        return

    intento = int(intento)
    if intento < 1 or intento > 100:
        lbl_resultado.config(text="El número debe estar entre 1 y 100.", fg="red")
        return

    intentos_restantes -= 1
    lbl_intentos.config(text=f"Intentos restantes: {intentos_restantes}")

    if intento == numero_secreto:
        lbl_resultado.config(text="¡Correcto! Has adivinado el número.", fg="#00FF00")
        btn_adivinar.config(state=tk.DISABLED)  # Deshabilitar el botón después de ganar
    elif intento < numero_secreto:
        lbl_resultado.config(text="Demasiado bajo. Intenta con un número más alto.", fg="#FF9933")
    else:
        lbl_resultado.config(text="Demasiado alto. Intenta con un número más bajo.", fg="#FF9933")

    if intentos_restantes == 0 and intento != numero_secreto:
        lbl_resultado.config(text=f"Has perdido. El número era {numero_secreto}.", fg="red")
        btn_adivinar.config(state=tk.DISABLED)  # Deshabilitar el botón después de perder

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Juego: Adivina el Número")
ventana.geometry("500x400")
ventana.configure(bg="#0F172A")  # Fondo azul oscuro

# Título del juego
titulo = tk.Label(ventana, text="¡Adivina el Número!", font=("Arial", 24, "bold"), bg="#0F172A", fg="#00FFFF")
titulo.pack(pady=20)

# Indicaciones
indicaciones = tk.Label(ventana, text="Adivina un número entre 1 y 100.\nTienes 10 intentos.",
                         font=("Arial", 14), bg="#0F172A", fg="#A7F3D0")
indicaciones.pack(pady=10)

# Campo para ingresar el número
entrada_numero = tk.Entry(ventana, font=("Arial", 16), justify="center", bg="#1E293B", fg="#E0E0E0")
entrada_numero.pack(pady=10)

# Botón para verificar el intento
btn_adivinar = tk.Button(ventana, text="Adivinar", font=("Arial", 16), bg="#2563EB", fg="#E0E0E0", 
                         command=verificar_intento)
btn_adivinar.pack(pady=10)

# Mostrar resultado
lbl_resultado = tk.Label(ventana, text="¡Comienza el juego! Intenta adivinar el número.", font=("Arial", 14),
                         bg="#0F172A", fg="#00FF00")
lbl_resultado.pack(pady=20)

# Mostrar intentos restantes
lbl_intentos = tk.Label(ventana, text=f"Intentos restantes: 10", font=("Arial", 14), bg="#0F172A", fg="#00FFFF")
lbl_intentos.pack(pady=10)

# Botón para reiniciar el juego
btn_reiniciar = tk.Button(ventana, text="Reiniciar", font=("Arial", 16), bg="#4C51BF", fg="#E0E0E0",
                          command=reiniciar_juego)
btn_reiniciar.pack(pady=10)

# Inicializar el juego
numero_secreto = random.randint(1, 100)
intentos_restantes = 10

# Ejecutar la ventana
ventana.mainloop()
