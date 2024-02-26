"""
Combinaciones de un Conjunto: Implementa una función recursiva que muestre todas las combinaciones posibles de un conjunto dado.
"""

def subconjuntos(inicial, actual=[]):

    if not inicial:
        if actual == []:
            return
        print(actual)

    else:
        # Incluye el elemento actual en el subconjunto
        subconjuntos(inicial[1:], actual + [inicial[0]])
        
        # No incluye el elemento actual en el subconjunto
        subconjuntos(inicial[1:], actual)

# Pruebas
print("Subconjuntos de [1, 2, 3, 4]:")
subconjuntos([1, 2, 3, 4])

print("\nSubconjuntos de [1, 2, 3]:")
subconjuntos([1, 2, 3])
