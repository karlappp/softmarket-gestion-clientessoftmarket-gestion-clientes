from productos import Producto

producto1 = Producto("Laptop", 2500000)
producto1.mostrar_informacion()

print("\nProbando validacion de precios:")

try:
    producto2 = Producto("Teclado", -50000)
except ValueError as error:
    print("Error:", error)