from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
  
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento: str = nombre_establecimiento
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def registrar_producto(self, nuevo_producto: Producto) -> None:
        self.lista_productos.append(nuevo_producto)

    def registrar_cliente(self, nuevo_cliente: Cliente) -> None:
        self.lista_clientes.append(nuevo_cliente)

    def mostrar_informacion_general(self) -> None:
        print(f"=== SISTEMA DE GESTIÓN: {self.nombre_establecimiento.upper()} ===")
        
        print("\n--- MENÚ DE PRODUCTOS ---")
        if not self.lista_productos:
            print("No hay productos registrados.")
        for producto in self.lista_productos:
            print(producto)  
            
        print("\n--- CLIENTES REGISTRADOS ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
        for cliente in self.lista_clientes:
            print(cliente)  
        print("=" * (24 + len(self.nombre_establecimiento)))