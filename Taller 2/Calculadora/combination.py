#Funcion de combinacion
import math
from FloatNotAllowed import FloatNotAllowed
from NegativeIntegerNotAllowed import NegativeIntegerNotAllowed


def combinacion_con_repeticion(m, n): #O(n) 
    # Calcula la combinación con repetición utilizando la fórmula (m + n - 1)! / (n! * (m - 1)!)
    # Donde m es el número total de elementos y n es el número de elementos a seleccionar
    # Utiliza la función factorial del módulo math para calcular los factoriales necesarios
    # Utiliza también la función comb() del módulo math para calcular las combinaciones directamente
    
    if isinstance(m, float) or isinstance(n, float):
        raise FloatNotAllowed("No se permiten valores decimales.")

    # Verifica si los argumentos son negativos
    if m < 0 or n < 0:
        raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")
    
    return (math.factorial(m + n - 1)) // ((math.factorial(n)) * (math.factorial(m - 1))) #O(n)

def combinacion_sin_repeticion(m, n): 
    # La función comb() calcula el número de combinaciones de m elementos tomados de a n
    
    if isinstance(m, float) or isinstance(n, float):
        raise FloatNotAllowed("No se permiten valores decimales.")

    # Verifica si los argumentos son negativos
    if m < 0 or n < 0:
        raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")
    
    return math.comb(m, n) #O(n)
