import math

def principioMultiplicativo(numerosMultiplicativo): #O(n)
    listaNumeros = list(map(int, numerosMultiplicativo.split(","))) #Complejidad temporal: O(n) Complejidad espacial: O(1)

    if any(not isinstance(numero, int) for numero in listaNumeros): #O(n)
        return "Error, ingresaste un valor no numérico" #O(1)
      
    total = math.prod(listaNumeros) #Complejidad temporal: O(n) Complejidad espacial: O(1)

    return total #O(1)
