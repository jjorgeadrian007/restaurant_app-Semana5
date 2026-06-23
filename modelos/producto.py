class Producto:
  
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre: str = nombre
        self.precio: float = precio
        self.disponible: bool = disponible

    def __str__(self) -> str:
        if self.disponible == True:
            estado: str = "Disponible"
        else:
            estado: str = "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Estado: {estado}"
    
