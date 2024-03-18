#Funcion de permutacion

import math

def permutacion_con_repeticion(m, list):
  # Calcula la permutación con repetición utilizando la fórmula m! / (n1! * n2! * ... * nk!)
  # Donde m es el número total de elementos y n1, n2, ..., nk son las repeticiones de cada elemento
  # Utiliza la función factorial del módulo math para calcular los factoriales necesarios
  result = math.factorial(m)
  for i in list:
    result = result // math.factorial(i)
  return result

def permutacion_sin_repeticion(m):
    # calcula el factorial de m
    return math.factorial(m)