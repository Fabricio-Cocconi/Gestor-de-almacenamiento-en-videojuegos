# Proyecto: Optimización de Inventario en un Videojuego de Simulación de Tienda

## Integrantes
- **Fabricio Cocconi**
- **Daniel Gonzales**
- **Amparo Carrizo**
- **Alvaro Benicio**
- **Gerardo Catalas**

## Descripción del Proyecto
Este proyecto tiene como objetivo recrear un videojuego de simulación donde el jugador asume el rol de gestor de un local comercial. A través de una interfaz gráfica, el jugador puede:
- Comprar y vender productos.
- Controlar el presupuesto y las transacciones.
- Gestionar el inventario con un stock limitado y actualizado automáticamente.

El proyecto permite la experiencia de la toma de decisiones financieras y la optimización del inventario, simulando situaciones reales de manejo de recursos en una tienda.

## Estructura del Proyecto
El proyecto se divide en dos archivos principales:
- **`logica.py`**: Contiene las clases y funciones encargadas de manejar el inventario, presupuesto y lógica de compra y venta, incluyendo la asignación de stock inicial aleatorio y la incorporación de IVA en las ventas.
- **`menu.py`**: Contiene la interfaz gráfica del usuario (GUI) desarrollada en Tkinter, permitiendo la interacción del usuario con el sistema de inventario mediante un menú visual.

## Inicio de Sesión
Para acceder al sistema, el usuario debe autenticarse con las siguientes credenciales:

- **Usuario**: `usuario`
- **Contraseña**: `1234`

Al ingresar, el usuario puede ver el presupuesto inicial, realizar compras o ventas, y revisar el estado del inventario.

## Requisitos de Instalación
Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes extensiones de Python:

1. **NumPy**: Para manejar cálculos numéricos.
2. **Tkinter**: Para crear la interfaz gráfica.

### Comandos para instalar extensiones
Ejecuta los siguientes comandos en Git Bash para instalar las dependencias:

```bash
pip install numpy
