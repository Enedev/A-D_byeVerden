
class CountingIsNotPossible(Exception):
    def __init__(self, mensaje=" No es posible realizar el conteo con los valores ingresados ..."):
        super().__init__(mensaje)
