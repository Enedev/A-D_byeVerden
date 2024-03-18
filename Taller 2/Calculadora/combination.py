#Funcion de combinacion
import math

def combinacion_con_repeticion(m, n): #O(n) 
    # Calcula la combinación con repetición utilizando la fórmula (m + n - 1)! / (n! * (m - 1)!)
    # Donde m es el número total de elementos y n es el número de elementos a seleccionar
    # Utiliza la función factorial del módulo math para calcular los factoriales necesarios
    # Utiliza también la función comb() del módulo math para calcular las combinaciones directamente 
    return (math.factorial(m + n - 1)) // ((math.factorial(n)) * (math.factorial(m - 1))) #Complejidad temporal: O(n) Complejidad espacial: O(1)

def combinacion_sin_repeticion(m, n): 
    # La función comb() calcula el número de combinaciones de m elementos tomados de a n
    return math.comb(m, n) #O(n)