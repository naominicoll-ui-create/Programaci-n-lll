"Cuenta Bancaria"
import tkinter as tk
from tkinter import messagebox

# Datos iniciales del usuario
nombre_usuario = "Naomi Muñoz"
numero_cuenta = "1234567890"
saldo = 900.0
historial = []

# Funciones
def consultar_saldo():
    """Muestra el saldo actual."""
    mensaje = f"Su saldo actual es: ${saldo:.2f}"
    historial.append("Consulta de saldo")
    messagebox.showinfo("Consulta de Saldo", mensaje)

def transferir():
    """Abre una ventana para realizar transferencias."""
    def realizar_transferencia():
        try:
            monto = float(entrada_monto.get())
            cuenta_destino = entrada_cuenta.get()
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
            if not cuenta_destino.strip():
                raise ValueError("Debe ingresar un número de cuenta válido.")
            global saldo
            if monto > saldo:
                raise ValueError("Fondos insuficientes.")
            saldo -= monto
            historial.append(f"Transferencia: -${monto:.2f} a la cuenta {cuenta_destino}")
            messagebox.showinfo("Transferencia", f"Transferencia exitosa de ${monto:.2f} a la cuenta {cuenta_destino}\nSaldo actual: ${saldo:.2f}")
            ventana_transferencia.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    ventana_transferencia = tk.Toplevel(root)
    ventana_transferencia.title("Realizar Transferencia")
    ventana_transferencia.configure(bg="lightblue")
    tk.Label(ventana_transferencia, text="Ingrese el número de cuenta destino:", bg="lightblue").pack(pady=10)
    entrada_cuenta = tk.Entry(ventana_transferencia)
    entrada_cuenta.pack(pady=5)
    tk.Label(ventana_transferencia, text="Ingrese el monto a transferir:", bg="lightblue").pack(pady=10)
    entrada_monto = tk.Entry(ventana_transferencia)
    entrada_monto.pack(pady=5)
    tk.Button(ventana_transferencia, text="Transferir", command=realizar_transferencia, bg="yellow").pack(pady=10)

def depositar():
    """Abre una ventana para realizar depósitos."""
    def realizar_deposito():
        try:
            monto = float(entrada_monto.get())
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
            global saldo
            saldo += monto
            historial.append(f"Depósito: +${monto:.2f}")
            messagebox.showinfo("Depósito", f"Depósito exitoso: ${monto:.2f}\nSaldo actual: ${saldo:.2f}")
            ventana_deposito.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduzca un monto válido.")
    
    ventana_deposito = tk.Toplevel(root)
    ventana_deposito.title("Depositar Dinero")
    ventana_deposito.configure(bg="lightgreen")
    tk.Label(ventana_deposito, text="Ingrese el monto a depositar:", bg="lightgreen").pack(pady=10)
    entrada_monto = tk.Entry(ventana_deposito)
    entrada_monto.pack(pady=5)
    tk.Button(ventana_deposito, text="Depositar", command=realizar_deposito, bg="yellow").pack(pady=10)

def retirar():
    """Abre una ventana para realizar retiros."""
    def realizar_retiro():
        try:
            monto = float(entrada_monto.get())
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
            global saldo
            if monto > saldo:
                raise ValueError("Fondos insuficientes.")
            saldo -= monto
            historial.append(f"Retiro: -${monto:.2f}")
            messagebox.showinfo("Retiro", f"Retiro exitoso: ${monto:.2f}\nSaldo restante: ${saldo:.2f}")
            ventana_retiro.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    ventana_retiro = tk.Toplevel(root)
    ventana_retiro.title("Retirar Dinero")
    ventana_retiro.configure(bg="lightcoral")
    tk.Label(ventana_retiro, text="Ingrese el monto a retirar:", bg="lightcoral").pack(pady=10)
    entrada_monto = tk.Entry(ventana_retiro)
    entrada_monto.pack(pady=5)
    tk.Button(ventana_retiro, text="Retirar", command=realizar_retiro, bg="orange").pack(pady=10)

def ver_historial():
    """Muestra el historial de transacciones."""
    if not historial:
        messagebox.showinfo("Historial", "No hay transacciones registradas.")
        return
    historial_texto = "\n".join(historial)
    messagebox.showinfo("Historial de Transacciones", historial_texto)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Cuenta Bancaria")
root.geometry("300x450")
root.configure(bg="gray")  # Fondo gris

# Etiquetas y botones principales
tk.Label(root, text="Bienvenido", bg="gray", font=("Arial", 14, "bold"), fg="white").pack(pady=10)
tk.Label(root, text="Cuenta de Ahorro", bg="gray", font=("Arial", 12), fg="white").pack(pady=5)
tk.Label(root, text=f"Usuario: {nombre_usuario}", bg="gray", font=("Arial", 12), fg="white").pack(pady=5)
tk.Label(root, text=f"Número de cuenta: {numero_cuenta}", bg="gray", font=("Arial", 12), fg="white").pack(pady=5)
tk.Button(root, text="Consultar Saldo", command=consultar_saldo, bg="lightgreen", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Depositar Dinero", command=depositar, bg="lightblue", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Transferir Dinero", command=transferir, bg="lightyellow", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Retirar Dinero", command=retirar, bg="lightcoral", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Ver Historial", command=ver_historial, bg="yellow", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Salir", command=root.destroy, bg="red", font=("Arial", 12)).pack(pady=20)

# Inicia el loop principal de la interfaz
root.mainloop()
