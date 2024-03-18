#Interfaz de usuario

from combination import combinacion_con_repeticion, combinacion_sin_repeticion
from permutation import permutacion_con_repeticion, permutacion_sin_repeticion
from variation import variacion_con_repeticion, variacion_sin_repeticion

def determinar_tipo_problema(respuestas):
    # Lógica para determinar el tipo de problema basado en las respuestas dadas
    if respuestas[0] == 's':
        if respuestas[1] == 'n':
            if respuestas[2] == 'n':
                return "Variación ordinaria"
            elif respuestas[2] == 's':
                return "Variación con repetición"
        elif respuestas[1] == 's':
            if respuestas[2] == 'n':
                return "Permutación ordinaria"
            elif respuestas[2] == 's':
                return "Permutación con repetición"
    else:
        if respuestas[1] == 'n':
            if respuestas[2] == 'n':
                return "Combinación ordinaria"
            elif respuestas[2] == 's':
                return "Combinación con repetición"

def main():
    #Interfaz de inputs de usuarios 
    print("Resolución de problemas de conteo")
    print("Por favor, responda las siguientes preguntas:")
    respuesta_orden = input("1. ¿Importa el orden? (s/n): ").lower()
    respuesta_intervienen = input("2. ¿Intervienen todos los elementos? (s/n): ").lower()
    respuesta_repiten = input("3. ¿Se repiten los elementos? (s/n): ").lower()

    # Determinar el tipo de problema de conteo según las respuestas del usuario
    tipo_problema = determinar_tipo_problema((respuesta_orden, respuesta_intervienen, respuesta_repiten))
    print("Tipo de problema:", tipo_problema)
    # Dependiendo del tipo de problema, se ejecuta la solución correspondiente
    # Por cada tipo_problema hay que especificar alguna pregunta y luego el resultado lo da la función correspondiente
    if tipo_problema == "Variación ordinaria":
        m = int(input("Ingrese el número total de elementos (m): "))
        n = int(input("Ingrese el número de elementos a seleccionar (n): "))
        resultado = variacion_sin_repeticion(m, n)
    elif tipo_problema == "Variación con repetición":
        m = int(input("Ingrese el número total de elementos (m): "))
        n = int(input("Ingrese el número de veces que se pueden repetir los elementos (n): "))
        resultado = variacion_con_repeticion(m, n)
    elif tipo_problema == "Permutación ordinaria":
        m = int(input("Ingrese el número total de elementos (m): "))
        resultado = permutacion_sin_repeticion(m)
    elif tipo_problema == "Permutación con repetición":
        m = int(input("Ingrese el número total de elementos (m): "))
        elementos_repetidos = list(map(int, input("Ingrese la cantidad de repeticiones de cada elemento separadas por espacios: ").split()))
        resultado = permutacion_con_repeticion(m, elementos_repetidos)
    elif tipo_problema == "Combinación ordinaria":
        m = int(input("Ingrese el número total de elementos (m): "))
        n = int(input("Ingrese el número de elementos a seleccionar (n): "))
        resultado = combinacion_sin_repeticion(m, n)
    elif tipo_problema == "Combinación con repetición":
        m = int(input("Ingrese el número total de elementos (m): "))
        n = int(input("Ingrese el número de elementos a seleccionar (n): "))
        resultado = combinacion_con_repeticion(m, n)

    print("El resultado es:", resultado)

if __name__ == "__main__":
    main()
