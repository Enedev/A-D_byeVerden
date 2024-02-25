def subconjuntos(inicial, actual=[]):

  if not inicial:
      if actual == []:
        return
      print(actual)

  else:
      subconjuntos(inicial[1:], actual + [inicial[0]])
      subconjuntos(inicial[1:], actual)
      
subconjuntos([1, 2, 3, 4])
