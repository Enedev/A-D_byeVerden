import math
from FloatNotAllowed import FloatNotAllowed
from NegativeIntegerNotAllowed import NegativeIntegerNotAllowed

def principioAditivo(numeros):  
    listaNumeros = list(map(int, numeros.split(",")))

    if any(not isinstance(numero, int) for numero in listaNumeros):
        raise FloatNotAllowed("No se permiten valores decimales.")

    if any(numero < 0 for numero in listaNumeros):
        raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")

    total = math.fsum(listaNumeros)

    return total
