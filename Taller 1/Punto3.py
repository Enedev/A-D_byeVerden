# Punto 3
# Permutaciones de una Cadena: Escribe una función que genere todas las permutaciones posibles de una cadena de caracteres.
def permutaciones(cadena): 
    
    if len(cadena) <= 1: # O(1)
        return [cadena] # O(1)
    resultado = [] # O(1) # Complejidad espacial: O(n)

    pila = [(cadena, '')] # O(1) # Complejidad espacial: O(n)
    
    while pila: #O(n)
        actual, permutacion_parcial = pila.pop() # O(n) # Complejidad espacial:O(n)

        if len(actual) == 1:#O(n)
            resultado.append(permutacion_parcial + actual) # O(n)
            
        else:#O(n)
            for i in range(len(actual)): # O(n)
                siguiente_permutacion = actual[:i] + actual[i+1:] # O(n) # Complejidad espacial: O(n)
                pila.append((siguiente_permutacion, permutacion_parcial + actual[i])) #O(n)

    return resultado # O(1)

#pruebas
cadena = "123" # O(1) # O(1)
print(permutaciones(cadena))

cadena = "456" # O(1) # O(1)
print(permutaciones(cadena))
