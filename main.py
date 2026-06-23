# Importaciones correctas entre módulos utilizando la estructura de paquetes
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_sistema() -> None:

    mi_restaurante = Restaurante("Sabores Auténticos")

    producto_uno = Producto("Asado de Tira", 18.50, True)
    producto_dos = Producto("Limonada Imperial", 3.75, True)
    producto_tres = Producto("Postre de Tres Leches", 4.20, False)

    cliente_uno = Cliente("1723456789", "Carlos Andrade", 5)
    cliente_dos = Cliente("0912345678", "María Fernanda Torres", 12)

    mi_restaurante.registrar_producto(producto_uno)
    mi_restaurante.registrar_producto(producto_dos)
    mi_restaurante.registrar_producto(producto_tres)

    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    mi_restaurante.mostrar_informacion_general()


ejecutar_sistema()