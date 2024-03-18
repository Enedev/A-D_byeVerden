import math

def principioAditivo(numeros):  #O(n)
    listaNumeros = list(map(int, numeros.split(","))) #Complejidad temporal: O(n) Complejidad espacial: O(1)

    if any(not isinstance(numero, int) for numero in listaNumeros):
        return "Error, ingresaste un valor no numérico" #O(1)

    total = math.fsum(listaNumeros) #Complejidad temporal: O(n) Complejidad espacial: O(1) 

    return total #O(1)
