class Cliente:

    def __init__(self, cedula: str, nombre_completo: str, visitas_realizadas: int):
        # Atributos con identificadores descriptivos
        self.cedula: str = cedula
        self.nombre_completo: str = nombre_completo
        self.visitas_realizadas: int = visitas_realizadas

    def __str__(self) -> str:
        return f"Cliente: {self.nombre_completo} (Cédula: {self.cedula}) | Visitas: {self.visitas_realizadas}"
    