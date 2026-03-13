# Programa: Inventario de productos
# Permite registrar varios productos, validar datos
# y calcular el costo total de cada uno.

inventario = []  # Lista donde se guardarán los productos

# Función para pedir precio válido
def pedir_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error: el precio no puede ser negativo.")
            else:
                return precio
        except ValueError:
            print("Error: debe ingresar un número válido.")


# Función para pedir cantidad válida
def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("Error: la cantidad no puede ser negativa.")
            else:
                return cantidad
        except ValueError:
            print("Error: debe ingresar un número entero válido.")


# Ciclo para registrar productos
while True:

    print("\n--- Registrar nuevo producto ---")

    # Entrada de datos
    nombre = input("Ingrese el nombre del producto: ")
    precio = pedir_precio()
    cantidad = pedir_cantidad()

    # Procesamiento
    costo_total = precio * cantidad

    # Guardar en el inventario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total": costo_total
    }

    inventario.append(producto)

    # Mostrar resultado del producto registrado
    print("\nProducto registrado:")
    print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

    # Preguntar si desea agregar otro producto
    continuar = input("\n¿Desea agregar otro producto? (s/n): ").lower()

    if continuar != "s":
        break

# Mostrar inventario completo
print("\n===== INVENTARIO REGISTRADO =====")

for p in inventario:
    print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']} | Total: {p['total']}")

print("=================================")

# Comentario final:
# Este programa permite registrar múltiples productos en un inventario.
# El usuario ingresa nombre, precio y cantidad. El sistema valida los
# datos, calcula el costo total y guarda cada producto en una lista.
# Finalmente muestra todo el inventario registrado.