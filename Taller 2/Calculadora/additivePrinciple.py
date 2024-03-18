def principioAditivo(numeros):
    listaNumeros = list(map(int, numeros.split(",")))

    if any(not isinstance(numero, int) for numero in listaNumeros):
        return "Error, ingresaste un valor no numérico"

    total = math.fsum(listaNumeros)

    return total
