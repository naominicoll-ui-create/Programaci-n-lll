#Analizar emociones
import tkinter as tk
from tkinter import messagebox

# Palabras clave para emociones
emociones_positivas = ["feliz", "contento", "alegría", "amor", "genial", "excelente", "enamorado", "euforia", "felicidad"]
emociones_negativas = ["triste", "mal", "deprimido", "odio", "malo", "horrible", "terrible", "enojado", "solo", "pesimo", "frustado", "con ganas de llorar", "dolor"]
emociones_neutrales = ["normal", "ok", "neutral", "bien", "nada", "x", "relajado", "estable", "indiferente"]

# Función para analizar emociones y abrir la segunda pantalla
def analizar_emociones ():
    texto = text_box.get("1.0", "end-1c").lower()  # Obtener el texto del bloc de notas y convertir a minúsculas

    if any(palabra in texto for palabra in emociones_positivas):
        emociones = "Positivo"
        frase = "Qué hermoso verte tan lleno/a de vida. Tus buenas vibras iluminan todo a tu alrededor 😊"
    elif any(palabra in texto for palabra in emociones_negativas):
        emociones = "Negativo"
        frase = "No hay oscuridad que dure para siempre. Habrá un nuevo amanecer para ti."
    elif any(palabra in texto for palabra in emociones_neutrales):
        emociones = "Neutral"
        frase = "Está bien estar en un lugar intermedio. El equilibrio también es una forma de estar bien."
    else:
        emociones = "Indeterminado"
        frase = "No se pudo determinar tu estado de ánimo 🤔"

    mostrar_segunda_pantalla(emociones, frase)

# Función para mostrar la segunda pantalla con el sentimiento analizado
def mostrar_segunda_pantalla(emociones, frase):
    ventana.withdraw()  # Ocultar la ventana principal

    segunda_pantalla = tk.Toplevel()
    segunda_pantalla.title("Resultado del Análisis")
    segunda_pantalla.geometry("400x300")
    segunda_pantalla.configure(bg="#FFFACD")

    # Mostrar el emociones analizado
    etiqueta_emociones = tk.Label(segunda_pantalla, text=f"Tu estado de ánimo es: {emociones}", font=("Arial", 16, "bold"), bg="#FFFACD", fg="#FF6347")
    etiqueta_emociones.pack(pady=20)

    # Botón para mostrar la frase en una tercera pantalla
    boton_frase = tk.Button(segunda_pantalla, text="Frase que debes leer", font=("Arial", 12, "bold"), bg="#FF6347", fg="white",
                            command=lambda: mostrar_tercera_pantalla(frase))
    boton_frase.pack(pady=10)

    # Botón para cerrar la segunda pantalla y volver a la principal
    boton_volver = tk.Button(segunda_pantalla, text="Volver", font=("Arial", 12), bg="#87CEEB", fg="black",
                            command=lambda: [segunda_pantalla.destroy(), ventana.deiconify()])
    boton_volver.pack(pady=10)

# Función para mostrar la tercera pantalla con la frase
def mostrar_tercera_pantalla(frase):
    tercera_pantalla = tk.Toplevel()
    tercera_pantalla.title("Frase para ti")
    tercera_pantalla.geometry("400x200")
    tercera_pantalla.configure(bg="#F0E68C")

    # Mostrar la frase
    etiqueta_frase = tk.Label(tercera_pantalla, text=frase, font=("Arial", 14, "italic"), bg="#F0E68C", fg="#2E8B57", wraplength=350, justify="center")
    etiqueta_frase.pack(pady=20)

    # Botón para cerrar la tercera pantalla
    boton_cerrar = tk.Button(tercera_pantalla, text="Cerrar", font=("Arial", 12), bg="#FF6347", fg="white", command=tercera_pantalla.destroy)
    boton_cerrar.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador de emociones")
ventana.geometry("600x400")
ventana.configure(bg="#87CEEB")

# Encabezado
titulo = tk.Label(ventana, text="Analiza tu emociones", font=("Arial", 24, "bold"), fg="#FF6347", bg="#87CEEB")
titulo.pack(pady=20)

# Cuadro de texto
text_box = tk.Text(ventana, height=8, width=60, bg="#FFFACD", fg="black", font=("Arial", 12), wrap="word", bd=5, relief="solid")
text_box.pack(pady=20)

# Botón para analizar
boton_analizar = tk.Button(ventana, text="Analizar emociones", font=("Arial", 14, "bold"), bg="#FF6347", fg="white", command=analizar_emociones)
boton_analizar.pack(pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()