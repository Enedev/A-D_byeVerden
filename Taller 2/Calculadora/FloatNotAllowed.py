
class FloatNotAllowed(Exception):
    def __init__(self, mensaje="No se permiten valores decimales."):
        super().__init__(mensaje)
