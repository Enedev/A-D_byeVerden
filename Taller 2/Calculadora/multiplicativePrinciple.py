import math

def principioMultiplicativo(numerosMultiplicativo):
    listaNumeros = list(map(int, numerosMultiplicativo.split(",")))

    if any(not isinstance(numero, int) for numero in listaNumeros):
        return "Error, ingresaste un valor no numérico"
      
    total = math.prod(listaNumeros)

    return total
