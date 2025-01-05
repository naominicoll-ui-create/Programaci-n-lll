#gestion de las calificaciones

import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox

# Clase Alumno
class Alumno:
    def __init__(self, dni, apellidos, nombre, nota):
        self.dni = dni
        self.apellidos = apellidos
        self.nombre = nombre
        self.nota = nota
        self.calificacion = self.calcular_calificacion()

    def calcular_calificacion(self):
        if self.nota < 5:
            return "SS"  # Suspenso
        elif 5 <= self.nota <= 6.9:
            return "SS"  # Suspenso
        elif 7 <= self.nota < 9:
            return "NT"  # Notable
        elif self.nota >= 9:
            return "SB"  # Sobresaliente

    def modificar_nota(self, nueva_nota):
        self.nota = nueva_nota
        self.calificacion = self.calcular_calificacion()

    def __str__(self):
        return f"{self.dni} {self.apellidos}, {self.nombre} {self.nota} {self.calificacion}"


# Clase para gestionar los alumnos
class GestionCalificaciones:
    def __init__(self):
        self.alumnos = {}

    def agregar_alumno(self, dni, apellidos, nombre, nota):
        if dni in self.alumnos:
            return "Error: Ya existe un alumno con ese DNI."
        nuevo_alumno = Alumno(dni, apellidos, nombre, nota)
        self.alumnos[dni] = nuevo_alumno
        return "Alumno agregado correctamente."

    def eliminar_alumno(self, dni):
        if dni in self.alumnos:
            del self.alumnos[dni]
            return "Alumno eliminado correctamente."
        return "Error: No existe un alumno con ese DNI."

    def consultar_alumno(self, dni):
        if dni in self.alumnos:
            alumno = self.alumnos[dni]
            return f"{alumno.dni} {alumno.apellidos}, {alumno.nombre} {alumno.nota} {alumno.calificacion}"
        return "Error: No existe un alumno con ese DNI."

    def modificar_nota(self, dni, nueva_nota):
        if dni in self.alumnos:
            self.alumnos[dni].modificar_nota(nueva_nota)
            return "Nota modificada correctamente."
        return "Error: No existe un alumno con ese DNI."

    def mostrar_alumnos(self):
        if not self.alumnos:
            return "No hay alumnos registrados."
        return "\n".join(str(alumno) for alumno in self.alumnos.values())

    def mostrar_suspensos(self):
        suspensos = [alumno for alumno in self.alumnos.values() if alumno.calificacion == "SS"]
        if not suspensos:
            return "No hay alumnos suspensos."
        return "\n".join(str(alumno) for alumno in suspensos)

    def mostrar_aprobados(self):
        aprobados = [alumno for alumno in self.alumnos.values() if alumno.calificacion != "SS"]
        if not aprobados:
            return "No hay alumnos aprobados."
        return "\n".join(str(alumno) for alumno in aprobados)

    def mostrar_candidatos_mh(self):
        mh = [alumno for alumno in self.alumnos.values() if alumno.nota == 10]
        if not mh:
            return "No hay alumnos candidatos a Matrícula de Honor."
        return "\n".join(str(alumno) for alumno in mh)


# Funciones de la interfaz gráfica
def agregar_alumno():
    dni = entry_dni.get()
    apellidos = entry_apellidos.get()
    nombre = entry_nombre.get()
    try:
        nota = float(entry_nota.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce una nota válida.")
        return
    mensaje = gestion.agregar_alumno(dni, apellidos, nombre, nota)
    messagebox.showinfo("Resultado", mensaje)
    mostrar_alumnos()

def eliminar_alumno():
    dni = entry_dni.get()
    mensaje = gestion.eliminar_alumno(dni)
    messagebox.showinfo("Resultado", mensaje)
    mostrar_alumnos()

def consultar_alumno():
    dni = entry_dni.get()
    mensaje = gestion.consultar_alumno(dni)
    messagebox.showinfo("Resultado", mensaje)

def modificar_nota():
    dni = entry_dni.get()
    try:
        nueva_nota = float(entry_nota.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce una nueva nota válida.")
        return
    mensaje = gestion.modificar_nota(dni, nueva_nota)
    messagebox.showinfo("Resultado", mensaje)
    mostrar_alumnos()

def mostrar_alumnos():
    resultado = gestion.mostrar_alumnos()
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, resultado)

def mostrar_suspensos():
    resultado = gestion.mostrar_suspensos()
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, resultado)

def mostrar_aprobados():
    resultado = gestion.mostrar_aprobados()
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, resultado)

def mostrar_candidatos_mh():
    resultado = gestion.mostrar_candidatos_mh()
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, resultado)


# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestión de Calificaciones de Alumnos")
root.geometry("600x500")
root.config(bg="gold")  # Fondo dorado

# Crear objeto de gestión de alumnos
gestion = GestionCalificaciones()

# Widgets de la interfaz gráfica
label_dni = tk.Label(root, text="DNI:", fg="black", bg="gold", font=("Arial", 12, "bold"))
label_dni.grid(row=0, column=0, padx=10, pady=10)

entry_dni = tk.Entry(root, font=("Arial", 12), bd=2)
entry_dni.grid(row=0, column=1, padx=10, pady=10)

label_apellidos = tk.Label(root, text="Apellidos:", fg="black", bg="gold", font=("Arial", 12, "bold"))
label_apellidos.grid(row=1, column=0, padx=10, pady=10)

entry_apellidos = tk.Entry(root, font=("Arial", 12), bd=2)
entry_apellidos.grid(row=1, column=1, padx=10, pady=10)

label_nombre = tk.Label(root, text="Nombre:", fg="black", bg="gold", font=("Arial", 12, "bold"))
label_nombre.grid(row=2, column=0, padx=10, pady=10)

entry_nombre = tk.Entry(root, font=("Arial", 12), bd=2)
entry_nombre.grid(row=2, column=1, padx=10, pady=10)

label_nota = tk.Label(root, text="Nota:", fg="black", bg="gold", font=("Arial", 12, "bold"))
label_nota.grid(row=3, column=0, padx=10, pady=10)

entry_nota = tk.Entry(root, font=("Arial", 12), bd=2)
entry_nota.grid(row=3, column=1, padx=10, pady=10)

# Botones con colores personalizados
btn_agregar = tk.Button(root, text="Agregar Alumno", command=agregar_alumno, fg="white", bg="black", font=("Arial", 12))
btn_agregar.grid(row=4, column=0, padx=10, pady=10)

btn_eliminar = tk.Button(root, text="Eliminar Alumno", command=eliminar_alumno, fg="white", bg="darkred", font=("Arial", 12))
btn_eliminar.grid(row=4, column=1, padx=10, pady=10)

btn_consultar = tk.Button(root, text="Consultar Alumno", command=consultar_alumno, fg="white", bg="green", font=("Arial", 12))
btn_consultar.grid(row=5, column=0, padx=10, pady=10)

btn_modificar = tk.Button(root, text="Modificar Nota", command=modificar_nota, fg="white", bg="blue", font=("Arial", 12))
btn_modificar.grid(row=5, column=1, padx=10, pady=10)

btn_mostrar = tk.Button(root, text="Mostrar Todos", command=mostrar_alumnos, fg="white", bg="purple", font=("Arial", 12))
btn_mostrar.grid(row=6, column=0, padx=10, pady=10)

btn_suspensos = tk.Button(root, text="Suspensos", command=mostrar_suspensos, fg="white", bg="orange", font=("Arial", 12))
btn_suspensos.grid(row=6, column=1, padx=10, pady=10)

btn_aprobados = tk.Button(root, text="Aprobados", command=mostrar_aprobados, fg="white", bg="yellow", font=("Arial", 12))
btn_aprobados.grid(row=7, column=0, padx=10, pady=10)

btn_mh = tk.Button(root, text="Candidatos MH", command=mostrar_candidatos_mh, fg="white", bg="cyan", font=("Arial", 12))
btn_mh.grid(row=7, column=1, padx=10, pady=10)

# Área de texto para mostrar resultados
text_area = tk.Text(root, height=10, width=50, font=("Arial", 12), bg="black", fg="white", bd=2)
text_area.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
