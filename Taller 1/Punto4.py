"""Combinaciones de un Conjunto: Implementa una función recursiva que muestre todas las combinaciones posibles de un conjunto dado. 
Por ejemplo, dado el conjunto {1,2,3} la función debería retornar todas las subconjuntos posibles."""

def subconjuntos(inicial, actual=[]):
  if not inicial:
      if actual == []:
        return
      print(actual)

  else:
      subconjuntos(inicial[1:], actual + [inicial[0]])
      subconjuntos(inicial[1:], actual)

#Pruebas
subconjuntos([1, 2, 3, 4])
subconjuntos([1, 2, 3])
