import tkinter as tk
from tkinter import messagebox
from logica import Inventario

# Crear una instancia de Inventario
inventario = Inventario()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Gestión de Inventarios")

# Ventana de inicio de sesión
login_window = tk.Toplevel(root)
login_window.title("Inicio de Sesión")
login_window.geometry("300x200")

usuario_correcto = "usuario"
contrasena_correcta = "1234"

# Función para mostrar mensajes en ventanas emergentes grandes
def mostrar_mensaje(titulo, mensaje):
    mensaje_ventana = tk.Toplevel(root)
    mensaje_ventana.title(titulo)
    mensaje_ventana.geometry("400x300")  # Ajustar el tamaño de la ventana

    tk.Label(mensaje_ventana, text=mensaje, justify="left", padx=10, pady=10).pack(expand=True)
    tk.Button(mensaje_ventana, text="Cerrar", command=mensaje_ventana.destroy).pack(pady=10)

# Función para validar el inicio de sesión
def validar_login():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        login_window.destroy()
        mostrar_mensaje("Inicio de Sesión Exitoso", "Bienvenido al sistema de gestión de inventarios.")
        presupuesto_label.config(text=f"Presupuesto actual: ${inventario.presupuesto}")
        main_menu()  # Mostrar el menú principal después del login
    else:
        mostrar_mensaje("Error", "Nombre de usuario o contraseña incorrectos.")

# Función para mostrar el menú principal
def main_menu():
    tk.Button(root, text="Ver estado del inventario", command=ver_inventario).pack(pady=5)
    tk.Button(root, text="Comprar productos", command=comprar_productos).pack(pady=5)
    tk.Button(root, text="Ver precios de mercado", command=ver_precios).pack(pady=5)
    tk.Button(root, text="Calcular precio final con IVA y ganancia", command=calcular_precio_final).pack(pady=5)
    tk.Button(root, text="Vender productos", command=vender_productos).pack(pady=5)
    tk.Button(root, text="Salir", command=root.quit).pack(pady=20)

# Función para ver el estado del inventario
def ver_inventario():
    inventario_texto = "--- Estado del Inventario ---\n"
    for producto, datos in inventario.ver_inventario().items():
        inventario_texto += f"{producto.capitalize()}: Stock actual = {datos['stock']} unidades\n"
    mostrar_mensaje("Estado del Inventario", inventario_texto)

# Función para comprar productos
def comprar_productos():
    total_compra = 0
    cantidades = {}

    # Crear una ventana para ingresar la cantidad de productos a comprar
    compra_ventana = tk.Toplevel(root)
    compra_ventana.title("Comprar Productos")
    compra_ventana.geometry("400x300")  # Ajustar el tamaño de la ventana
    tk.Label(compra_ventana, text="Ingrese las cantidades a comprar:").pack()

    # Crear un campo de entrada para cada producto
    entry_widgets = {}
    for producto, datos in inventario.ver_inventario().items():
        frame = tk.Frame(compra_ventana)
        frame.pack()
        tk.Label(frame, text=f"{producto.capitalize()} (Stock actual: {datos['stock']}):").pack(side="left")
        entry = tk.Entry(frame, width=5)
        entry.pack(side="right")
        entry_widgets[producto] = entry

    def confirmar_compra():
        total_compra = 0
        cantidades.clear()  # Limpiar las cantidades anteriores

        for producto, entry in entry_widgets.items():
            cantidad = int(entry.get() or 0)
            # Verificar que la cantidad no sea negativa
            if cantidad < 0:
                mostrar_mensaje("Error", f"La cantidad de {producto} no puede ser negativa.")
                compra_ventana.destroy()
                return

            try:
                # Comprobar si la compra es posible
                inventario.comprar_producto(producto, cantidad)
                total_compra += (cantidad * inventario.inventario[producto]["precio_mercado"])
                cantidades[producto] = cantidad  # Guardar la cantidad comprada
            except ValueError as e:
                mostrar_mensaje("Error", str(e))
                compra_ventana.destroy()
                return

        # Preguntar al usuario si desea confirmar la compra
        confirmar = messagebox.askyesno("Confirmar Compra", f"Costo total de la compra: ${total_compra}. ¿Desea confirmar?")
        if confirmar:
            # Actualizar el presupuesto
            presupuesto_label.config(text=f"Presupuesto actual: ${inventario.presupuesto}")
            mostrar_mensaje("Compra Exitosa", "Compra realizada exitosamente.")
        else:
            mostrar_mensaje("Compra Cancelada", "Compra cancelada.")
        compra_ventana.destroy()

    tk.Button(compra_ventana, text="Confirmar Compra", command=confirmar_compra).pack()

# Función para ver los precios de mercado
def ver_precios():
    precios_texto = "--- Precios de Mercado ---\n"
    for producto, datos in inventario.ver_inventario().items():
        precios_texto += f"{producto.capitalize()}: ${datos['precio_mercado']} por unidad\n"
    mostrar_mensaje("Precios de Mercado", precios_texto)

# Función para calcular precio final con IVA y ganancia
def calcular_precio_final():
    precio_final_texto = "--- Precio Final con IVA ---\n"
    for producto, datos in inventario.ver_inventario().items():
        precio_base = datos['precio_mercado']
        precio_final = precio_base * (1 + inventario.iva)  # Precio final incluye IVA
        precio_final_texto += f"{producto.capitalize()}: Precio base = ${precio_base}, Precio final = ${precio_final:.2f}\n"
    mostrar_mensaje("Precio Final con IVA", precio_final_texto)

# Función para vender productos
def vender_productos():
    # Crear una ventana para ingresar la cantidad de productos a vender
    venta_ventana = tk.Toplevel(root)
    venta_ventana.title("Vender Productos")
    venta_ventana.geometry("400x300")  # Ajustar el tamaño de la ventana
    tk.Label(venta_ventana, text="Ingrese la cantidad a vender:").pack()

    # Crear un campo de entrada para cada producto
    entry_widgets = {}
    for producto, datos in inventario.ver_inventario().items():
        frame = tk.Frame(venta_ventana)
        frame.pack()
        tk.Label(frame, text=f"{producto.capitalize()} (Stock actual: {datos['stock']}):").pack(side="left")
        entry = tk.Entry(frame, width=5)
        entry.pack(side="right")
        entry_widgets[producto] = entry

    def confirmar_venta():
        for producto, entry in entry_widgets.items():
            cantidad = int(entry.get() or 0)
            # Verificar que la cantidad no sea negativa
            if cantidad < 0:
                mostrar_mensaje("Error", f"La cantidad de {producto} no puede ser negativa.")
                venta_ventana.destroy()
                return

            try:
                # Comprobar si la venta es posible
                inventario.vender_producto(producto, cantidad)
            except ValueError as e:
                mostrar_mensaje("Error", str(e))
                venta_ventana.destroy()
                return

        # Actualizar el presupuesto
        presupuesto_label.config(text=f"Presupuesto actual: ${inventario.presupuesto}")
        mostrar_mensaje("Venta Exitosa", "Venta realizada exitosamente.")
        venta_ventana.destroy()

    tk.Button(venta_ventana, text="Confirmar Venta", command=confirmar_venta).pack()

# Elementos de la ventana de inicio de sesión
tk.Label(login_window, text="Nombre de usuario:").pack(pady=5)
usuario_entry = tk.Entry(login_window)
usuario_entry.pack(pady=5)
tk.Label(login_window, text="Contraseña:").pack(pady=5)
contrasena_entry = tk.Entry(login_window, show="*")
contrasena_entry.pack(pady=5)
tk.Button(login_window, text="Iniciar Sesión", command=validar_login).pack(pady=20)

# Label para mostrar el presupuesto
presupuesto_label = tk.Label(root, text="")
presupuesto_label.pack(pady=5)

root.mainloop()
