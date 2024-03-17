#Funcion de permutacion

import math

def permutacion_con_repeticion(m, list):
  result = math.factorial(m)
  for i in list:
    result = result // math.factorial(i)
  return result

def permutacion_sin_repeticion(m):
    return math.factorial(m)