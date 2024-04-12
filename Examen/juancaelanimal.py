#Punto 2 (2.0): Escribir un algoritmo que realice la multiplicación de los valores de un vector de forma recursiva.
def multiplicacion_recursiva(vector):
    if len(vector) == 1:
        return vector [0]
    else: 
        return vector[0] * multiplicacion_recursiva(vector [1:1])
    
vector = [1, 2, 3, 4]
resultado = multiplicacion_recursiva(vector)
print ("el resultado es:", resultado)


#Punto 3 (1.5): Se ordenan en una fila de 5 bolas negras, 2 bolas blancas y 3 bolas verdes. Si las bolas de igual color no se distinguen entre sí, ¿de cuantas formas posibles pueden ordenarse?
from math import factorial
total_bolas = 5 + 2 + 3 

negras = 5 
blancas = 2
verdes = 3

formas_posibles = factorial (total_bolas) / (factorial(negras) * factorial(blancas) * factorial(verdes))

print("El número de formas posibles", formas_posibles)
