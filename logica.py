import numpy as np

class Inventario:
    def __init__(self):
        # Inicialización de inventario con stock aleatorio entre 1 y 5
        self.inventario = {
            "pan": {"stock": np.random.randint(1, 6), "precio_mercado": 20},
            "fideos": {"stock": np.random.randint(1, 6), "precio_mercado": 15},
            "harina": {"stock": np.random.randint(1, 6), "precio_mercado": 12}
        }
        self.presupuesto = 500  # Presupuesto inicial
        self.capacidad_maxima = 10  # Capacidad máxima de almacenamiento por producto
        self.iva = 0.21  # IVA del 21%

    def ver_inventario(self):
        return self.inventario

    def comprar_producto(self, producto, cantidad):
        if producto in self.inventario:
            nuevo_stock = self.inventario[producto]["stock"] + cantidad
            # Limitar el stock a la capacidad máxima
            if nuevo_stock <= self.capacidad_maxima:
                costo_total = cantidad * self.inventario[producto]["precio_mercado"]
                if costo_total <= self.presupuesto:
                    self.presupuesto -= costo_total
                    self.inventario[producto]["stock"] = nuevo_stock
                else:
                    raise ValueError("No hay suficiente presupuesto para esta compra.")
            else:
                raise ValueError("No se puede exceder la capacidad máxima de almacenamiento.")
        else:
            raise ValueError("Producto no encontrado en el inventario.")

    def vender_producto(self, producto, cantidad):
        if producto in self.inventario:
            if cantidad <= self.inventario[producto]["stock"]:
                self.inventario[producto]["stock"] -= cantidad
                # Calcular ingresos por venta
                ingreso_producto = cantidad * self.calcular_precio_venta(producto)
                self.presupuesto += ingreso_producto
            else:
                raise ValueError("No hay suficiente stock para vender esa cantidad.")
        else:
            raise ValueError("Producto no encontrado en el inventario.")

    def calcular_precio_venta(self, producto):
        """Calcula el precio de venta, incluyendo IVA."""
        if producto in self.inventario:
            precio_base = self.inventario[producto]["precio_mercado"]
            return precio_base * (1 + self.iva)  # Precio de venta incluye IVA
        else:
            raise ValueError("Producto no encontrado en el inventario.")

    def calcular_precio_final(self, producto):
        """Calcula el precio final con IVA."""
        if producto in self.inventario:
            precio_base = self.inventario[producto]["precio_mercado"]
            precio_final = precio_base * (1 + self.iva)  # Precio final incluye IVA
            return precio_base, precio_final
        else:
            raise ValueError("Producto no encontrado en el inventario.")
