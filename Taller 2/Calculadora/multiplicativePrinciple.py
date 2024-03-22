import math
from FloatNotAllowed import FloatNotAllowed
from NegativeIntegerNotAllowed import NegativeIntegerNotAllowed

def principioMultiplicativo(numerosMultiplicativo):
    listaNumeros = list(map(int, numerosMultiplicativo.split(",")))

    if any(not isinstance(numero, int) for numero in listaNumeros):
        raise FloatNotAllowed("No se permiten valores decimales.")

    if any(numero < 0 for numero in listaNumeros):
        raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")

    total = math.prod(listaNumeros)

    return total
