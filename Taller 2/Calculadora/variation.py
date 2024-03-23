#Funcion de variacion
import math
from FloatNotAllowed import FloatNotAllowed
from NegativeIntegerNotAllowed import NegativeIntegerNotAllowed
from CountingIsNotPossible import CountingIsNotPossible

def variacion_sin_repeticion(m, n): #O(n)
    # La función perm() calcula la permutación de m elementos tomados de a n
    
    if n > m:
        raise CountingIsNotPossible("No es posible realizar el conteo con los valores ingresados ... ")
    
    if isinstance(m, float) or isinstance(n, float):
        raise FloatNotAllowed("No se permiten valores decimales.")

    # Verifica si los argumentos son negativos
    if m < 0 or n < 0:
        raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")
    
    return math.perm(m, n) #O(n)

def variacion_con_repeticion(m, n): #O(n)
    # Calcula la variación con repetición mediante la fórmula m^n
    # Donde m es el número total de elementos y n es el número de veces que se pueden repetir los elementos
    
    if n > m:
        raise CountingIsNotPossible("No es posible realizar el conteo con los valores ingresados ... ")
    
    if isinstance(m, float) or isinstance(n, float):
        raise FloatNotAllowed("No se permiten valores decimales.")

    # Verifica si los argumentos son negativos
    if m < 0 or n < 0:
        raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")
    
    return m ** n #O(n)
