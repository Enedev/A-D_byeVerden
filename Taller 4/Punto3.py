def encontrar_minimo(arr):
    if not isinstance(arr, list):
        raise TypeError("El argumento debe ser una lista")

    if len(arr) == 0:
        raise ValueError("La lista no puede estar vacía")

    for elemento in arr:
        if not isinstance(elemento, int):
            raise TypeError("La lista solo puede contener números enteros")

    if len(arr) == 1:
        return arr[0]

    medio = len(arr) // 2
    izquierda_medio = arr[:medio]
    derecho_medio = arr[medio:]

    minimo_izquierdo = encontrar_minimo(izquierda_medio)
    minimo_derecho = encontrar_minimo(derecho_medio)

    if minimo_izquierdo is None:
        return minimo_derecho
    elif minimo_derecho is None:
        return minimo_izquierdo
    else:
        return minimo_izquierdo if minimo_izquierdo < minimo_derecho else minimo_derecho


# Lista con elementos no enteros
lista_no_enteros = [8, 3, 6, 2, '7', 1, 5, 4]

# Lista vacía
lista_vacia = []

# Llamada con argumento que no es lista
otro_tipo = "no soy una lista"

try:
    encontrar_minimo(lista_no_enteros)
except TypeError as e:
    print("Excepción generada:", e)

try:
    encontrar_minimo(lista_vacia)
except ValueError as e:
    print("Excepción generada:", e)

try:
    encontrar_minimo(otro_tipo)
except TypeError as e:
    print("Excepción generada:", e)

