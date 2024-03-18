#Funcion de permutacion

import math

def permutacion_con_repeticion(m, list): #O(n)
  # Calcula la permutación con repetición utilizando la fórmula m! / (n1! * n2! * ... * nk!)
  # Donde m es el número total de elementos y n1, n2, ..., nk son las repeticiones de cada elemento
  # Utiliza la función factorial del módulo math para calcular los factoriales necesarios
  result = math.factorial(m) #Complejidad temporal: O(n) Complejidad espacial: O(n)
  for i in list: #O(n)
    result = result // math.factorial(i) #Complejidad temporal: O(n) Complejidad espacial: O(n)
  return result #0(n)

def permutacion_sin_repeticion(m): #O(n)
    # calcula el factorial de m
    return math.factorial(m) #O(n)