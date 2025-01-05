#Piedra, Papel, Tijera
import tkinter as tk
import random

# Funciones del juego
def jugar(eleccion_jugador):
    opciones = ["Piedra", "Papel", "Tijera"]
    eleccion_computadora = random.choice(opciones)

    # Mostrar elección de la computadora
    lbl_computadora.config(text=f"Computadora eligió: {eleccion_computadora}")

    # Determinar el resultado
    if eleccion_jugador == eleccion_computadora:
        resultado = "¡Empate!"
    elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel"):
        resultado = "¡Ganaste!"
        marcador_jugador.set(marcador_jugador.get() + 1)
    else:
        resultado = "¡Perdiste!"
        marcador_computadora.set(marcador_computadora.get() + 1)

    # Mostrar el resultado
    lbl_resultado.config(text=resultado, fg="green" if resultado == "¡Ganaste!" else "red")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel, Tijera")
ventana.geometry("400x600")
ventana.configure(bg="#f0e68c")  # Fondo amarillo claro

# Títulos y estilos
titulo = tk.Label(ventana, text="Piedra, Papel, Tijera", font=("Arial", 20, "bold"), bg="#f0e68c", fg="purple")
titulo.pack(pady=10)

# Marcadores
marcador_jugador = tk.IntVar(value=0)
marcador_computadora = tk.IntVar(value=0)

frame_marcadores = tk.Frame(ventana, bg="#f0e68c")
frame_marcadores.pack(pady=10)

tk.Label(frame_marcadores, text="Jugador:", font=("Arial", 14), bg="#f0e68c").grid(row=0, column=0, padx=10)
tk.Label(frame_marcadores, textvariable=marcador_jugador, font=("Arial", 14, "bold"), bg="#f0e68c").grid(row=0, column=1)

tk.Label(frame_marcadores, text="Computadora:", font=("Arial", 14), bg="#f0e68c").grid(row=0, column=2, padx=10)
tk.Label(frame_marcadores, textvariable=marcador_computadora, font=("Arial", 14, "bold"), bg="#f0e68c").grid(row=0, column=3)

# Opciones del jugador en cuadros (botones grandes)
frame_botones = tk.Frame(ventana, bg="#f0e68c")
frame_botones.pack(pady=20)

btn_piedra = tk.Button(frame_botones, text="Piedra", width=10, height=5, bg="#ff9999", font=("Arial", 14, "bold"),
                       command=lambda: jugar("Piedra"))
btn_piedra.grid(row=0, column=0, padx=20, pady=10)

btn_papel = tk.Button(frame_botones, text="Papel", width=10, height=5, bg="#99ff99", font=("Arial", 14, "bold"),
                      command=lambda: jugar("Papel"))
btn_papel.grid(row=0, column=1, padx=20, pady=10)

btn_tijera = tk.Button(frame_botones, text="Tijera", width=10, height=5, bg="#9999ff", font=("Arial", 14, "bold"),
                       command=lambda: jugar("Tijera"))
btn_tijera.grid(row=0, column=2, padx=20, pady=10)

# Mostrar elección de la computadora
lbl_computadora = tk.Label(ventana, text="Computadora eligió: ", font=("Arial", 14), bg="#f0e68c", fg="black")
lbl_computadora.pack(pady=20)

# Mostrar el resultado
lbl_resultado = tk.Label(ventana, text="", font=("Arial", 16, "bold"), bg="#f0e68c")
lbl_resultado.pack(pady=20)

# Bucle principal
ventana.mainloop()
