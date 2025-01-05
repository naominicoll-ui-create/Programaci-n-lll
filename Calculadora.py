#Calculadora
import tkinter as tk


def agregar_a_pantalla(valor):
    pantalla.insert(tk.END, valor)

def limpiar_pantalla():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        # Reemplazamos símbolos para evitar conflictos con Python
        expr = pantalla.get().replace('÷', '/').replace('×', '*')
        if '/0' in expr:  # Validación para evitar división por cero
            raise ZeroDivisionError("División por cero no permitida")
        resultado = eval(expr)  # Evalúa la expresión matemática
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error: División por 0")
    except Exception:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error: Entrada inválida")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(bg="pink")

# Crear la pantalla para mostrar el resultado
pantalla = tk.Entry(
    ventana, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="white", fg="black"
)
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Crear los botones y agregarlos a la cuadrícula
for (texto, fila, col) in botones:
    color_fondo = "purple"
    color_texto = "white"
    if texto == 'C':
        tk.Button(
            ventana, text=texto, width=10, height=3, font=("Arial", 18), bg=color_fondo, fg=color_texto,
            command=limpiar_pantalla
        ).grid(row=fila, column=col, padx=5, pady=5)
    elif texto == '=':
        tk.Button(
            ventana, text=texto, width=10, height=3, font=("Arial", 18), bg=color_fondo, fg=color_texto,
            command=calcular
        ).grid(row=fila, column=col, padx=5, pady=5)
    else:
        tk.Button(
            ventana, text=texto, width=10, height=3, font=("Arial", 18), bg=color_fondo, fg=color_texto,
            command=lambda t=texto: agregar_a_pantalla(t)
        ).grid(row=fila, column=col, padx=5, pady=5)

# Iniciar el bucle de la ventana
ventana.mainloop()