"Descuento"
# Solicitar el monto gastado por el cliente
monto = float(input("Ingresa el monto gastado en la tienda: $"))

# Verificar si aplica el descuento
if monto > 100:
    descuento = monto * 0.20
    monto_final = monto - descuento
    print(f"Aplica un descuento del 20%. El monto final es: ${monto_final:.2f}")
else:
    print(f"No aplica descuento. El monto final es: ${monto:.2f}")
