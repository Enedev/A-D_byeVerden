#Funcion de permutacion

import math
from FloatNotAllowed import FloatNotAllowed
from NegativeIntegerNotAllowed import NegativeIntegerNotAllowed


def permutacion_con_repeticion(m, list): #O(n)
  # Calcula la permutación con repetición utilizando la fórmula m! / (n1! * n2! * ... * nk!)
  # Donde m es el número total de elementos y n1, n2, ..., nk son las repeticiones de cada elemento
  # Utiliza la función factorial del módulo math para calcular los factoriales necesarios
  
  # Verifica si algún número en la lista es un valor decimal
  for num in list:
      if isinstance(num, float):
          raise FloatNotAllowed("No se permiten valores decimales.")

  # Verifica si m es un valor decimal
  if isinstance(m, float):
      raise FloatNotAllowed("No se permiten valores decimales.")

  # Verifica si algún número en la lista es negativo
  if any(num < 0 for num in list):
      raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")

  # Verifica si m es negativo
  if m < 0:
      raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")
      
  result = math.factorial(m) #Complejidad temporal: O(n) Complejidad espacial: O(n)
  for i in list: #O(n)
    result = result // math.factorial(i) #Complejidad temporal: O(n) Complejidad espacial: O(n)
  return result #0(1)


def permutacion_sin_repeticion(m): #O(n)
    # calcula el factorial de m
    
    # Verifica si los argumentos son flotantes
    if isinstance(m, float) or isinstance(m, float):
        raise FloatNotAllowed("No se permiten valores decimales.")

    # Verifica si los argumentos son negativos
    if m < 0:
        raise NegativeIntegerNotAllowed("No se permiten números enteros negativos.")
    return math.factorial(m) #O(n)
