"""Funciones para registrar y consultar productos de SoftMarket S.A.

Trabaja con la clase Producto definida en productos.py. El almacenamiento
es una lista en memoria (simulación, sin base de datos real).
"""

from productos import Producto

# Almacenamiento por defecto de los productos registrados.
_inventario = []


def registrar_producto(nombre, precio, inventario=None):
    """Crea un Producto, lo guarda en el inventario y lo devuelve.

    Lanza ValueError si el nombre está vacío o si el precio es negativo
    (esta última validación la hace la clase Producto).
    """
    if inventario is None:
        inventario = _inventario

    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre del producto no puede estar vacío")

    producto = Producto(nombre.strip(), precio)
    inventario.append(producto)
    return producto


def consultar_productos(inventario=None):
    """Devuelve una copia de la lista de productos registrados."""
    if inventario is None:
        inventario = _inventario
    return list(inventario)


def mostrar_productos(inventario=None):
    """Imprime la información de cada producto registrado."""
    productos = consultar_productos(inventario)
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        producto.mostrar_informacion()
        print("-" * 20)


if __name__ == "__main__":
    registrar_producto("Cuaderno", 4500)
    registrar_producto("Lápiz", 1200)
    mostrar_productos()
