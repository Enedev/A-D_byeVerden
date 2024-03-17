#Funcion de combinacion
import math

def combinacion_con_repeticion(m, n):
    return (math.factorial(m + n - 1)) // ((math.factorial(n)) * (math.factorial(m - 1)))

def combinacion_sin_repeticion(m, n):
    return math.comb(m, n)