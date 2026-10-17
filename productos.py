class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre

        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self.precio = precio

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Precio: $", self.precio)