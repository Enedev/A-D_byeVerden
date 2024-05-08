def encontrar_min(lista):
    if len(lista)==0:
        return None
    
    if len(lista)==1:
        return lista[0]
    
    mitad = len(lista)//2
    mitad_izq= lista[:mitad]
    mitad_der = lista[mitad:]
    
    min_izq= encontrar_min(mitad_izq)
    min_der= encontrar_min(mitad_der)
    
    if min_izq is None:
        return min_der
    elif min_der is None:
        return min_izq
    else: 
        return min_izq if min_izq < min_der else min_der
    
    
n = [3,9,4,5,1,7,8]
print("El valor mínimo de la lista es", encontrar_min(n))
