#Funcion de variacion
import math

def variacion_sin_repeticion(m, n):
    # La función perm() calcula la permutación de m elementos tomados de a n
    return math.perm(m, n)

def variacion_con_repeticion(m, n):
    # Calcula la variación con repetición mediante la fórmula m^n
    # Donde m es el número total de elementos y n es el número de veces que se pueden repetir los elementos
    return m ** n