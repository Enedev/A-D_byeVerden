
class NegativeIntegerNotAllowed(Exception):
    def __init__(self, mensaje="No se permiten números enteros negativos."):
        super().__init__(mensaje)
