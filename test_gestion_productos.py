import unittest

from gestion_productos import (
    consultar_productos,
    mostrar_productos,
    registrar_producto,
)
from productos import Producto


class TestGestionProductos(unittest.TestCase):
    def setUp(self):
        self.inventario = []

    def test_registrar_devuelve_producto_de_karla(self):
        p = registrar_producto("Cuaderno", 4500, self.inventario)
        self.assertIsInstance(p, Producto)
        self.assertEqual(p.nombre, "Cuaderno")
        self.assertEqual(p.precio, 4500)

    def test_consultar_devuelve_productos_registrados(self):
        registrar_producto("Cuaderno", 4500, self.inventario)
        registrar_producto("Lápiz", 1200, self.inventario)
        nombres = [p.nombre for p in consultar_productos(self.inventario)]
        self.assertEqual(nombres, ["Cuaderno", "Lápiz"])

    def test_consultar_sin_productos_devuelve_lista_vacia(self):
        self.assertEqual(consultar_productos(self.inventario), [])

    def test_consultar_devuelve_copia(self):
        registrar_producto("Cuaderno", 4500, self.inventario)
        consultar_productos(self.inventario).clear()
        self.assertEqual(len(self.inventario), 1)

    def test_precio_negativo_lanza_error_y_no_registra(self):
        with self.assertRaises(ValueError):
            registrar_producto("Regla", -1, self.inventario)
        self.assertEqual(self.inventario, [])

    def test_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            registrar_producto("   ", 100, self.inventario)

    def test_precio_cero_es_valido(self):
        p = registrar_producto("Muestra", 0, self.inventario)
        self.assertEqual(p.precio, 0)

    def test_mostrar_usa_mostrar_informacion(self):
        import io
        from contextlib import redirect_stdout
        registrar_producto("Cuaderno", 4500, self.inventario)
        salida = io.StringIO()
        with redirect_stdout(salida):
            mostrar_productos(self.inventario)
        self.assertIn("Nombre: Cuaderno", salida.getvalue())
        self.assertIn("Precio: $ 4500", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
