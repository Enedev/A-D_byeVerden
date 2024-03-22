#Interfaz de usuario

#Modularización
from combination import combinacion_con_repeticion, combinacion_sin_repeticion
from permutation import permutacion_con_repeticion, permutacion_sin_repeticion
from variation import variacion_con_repeticion, variacion_sin_repeticion
from additivePrinciple import principioAditivo
from multiplicativePrinciple import principioMultiplicativo
from NegativeIntegerNotAllowed import NegativeIntegerNotAllowed
from FloatNotAllowed import FloatNotAllowed
from AnswerNotValid import AnswerNotValid

def determinar_tipo_problema(respuestas): #O(1)
    # Lógica para determinar el tipo de problema basado en las respuestas dadas
    if respuestas[0] == 's': #O(1)
        if respuestas[1] == 'n': #O(1)
            if respuestas[2] == 'n': #O(1)
                return "Variación ordinaria" #O(1)
            elif respuestas[2] == 's': #O(1)
                return "Variación con repetición" #O(1)
        elif respuestas[1] == 's': #O(1)
            if respuestas[2] == 'n': #O(1)
                return "Permutación ordinaria" #O(1)
            elif respuestas[2] == 's': #O(1)
                return "Permutación con repetición" #O(1)
    else:
        if respuestas[1] == 'n': #O(1)
            if respuestas[2] == 'n': #O(1)
                return "Combinación ordinaria" #O(1)
            elif respuestas[2] == 's': #O(1)
                return "Combinación con repetición" #O(1)

def ui_AM (): #O(n)
    while True:
        try: 
            numeros = input("Ingrese el numero de posibilidades para cada uno, separados por coma :") #Complejidad espacial : O(1) # Complejidad temporal : O(1)
            pregunta = input("¿Pueden ocurrir al mismo tiempo? s/n").lower() #Complejidad espacial : O(1) # Complejidad temporal : O(1)
            if pregunta == "s": #O(1)
                resultado = principioMultiplicativo(numeros) #Complejidad espacial : O(1) # Complejidad temporal : O(n)
            else :
                resultado = principioAditivo(numeros) #Complejidad espacial : O(1) # Complejidad temporal : O(n)
            break # se sale del bucle si no se disparó ninguna excepción 
        
        except FloatNotAllowed:
            print("Error: No se permiten valores decimales.")
        
        except NegativeIntegerNotAllowed:
            print("Error: No se permiten números enteros negativos.")
        
        except ValueError:
            print("Error: Solo se pueden ingresar numeros enteros positivos ...")
        except Exception as e:
            print("Error:", e)
            
    print("El resultado es:", resultado) #O(1)

def main(): #O(n)
    while True:
        #Interfaz de inputs de usuarios 
        print("Resolución de problemas de conteo") #O(1)
        print("Por favor, responda las siguientes preguntas:") #O(1)
        respuesta_AM = input("Necesito resolver un problema con principio aditivo o multiplicativo? (s/n):  ").lower() #O(1)
        
        if respuesta_AM == "s": #O(1)
            return ui_AM() #O(n)
        if respuesta_AM == "n":
            print("Al no ser un principio aditivo o multiplicativo, responda las siguientes preguntas:") #O(1)
            respuesta_orden = input("1. ¿Importa el orden? (s/n): ").lower() #O(1)
            respuesta_intervienen = input("2. ¿Intervienen todos los elementos? (s/n): ").lower() #O(1)
            respuesta_repiten = input("3. ¿Se repiten los elementos? (s/n): ").lower()#O(1)

            
            try:
            
                # Determinar el tipo de problema de conteo según las respuestas del usuario
                tipo_problema = determinar_tipo_problema((respuesta_orden, respuesta_intervienen, respuesta_repiten)) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                print("Tipo de problema:", tipo_problema) #O(1)
                # Dependiendo del tipo de problema, se ejecuta la solución correspondiente
                # Por cada tipo_problema hay que especificar alguna pregunta y luego el resultado lo da la función correspondiente
            
                
                if tipo_problema == "Variación ordinaria": #O(1)
                    m = int(input("Ingrese el número total de elementos (m): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    n = int(input("Ingrese el número de elementos a seleccionar (n): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    resultado = variacion_sin_repeticion(m, n) #Complejidad espacial : O(n) # Complejidad temporal : O(n)
                elif tipo_problema == "Variación con repetición": #O(1)
                    m = int(input("Ingrese el número total de elementos (m): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    n = int(input("Ingrese el número de veces que se pueden repetir los elementos (n): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    resultado = variacion_con_repeticion(m, n) #Complejidad espacial : O(n) # Complejidad temporal : O(n)
                elif tipo_problema == "Permutación ordinaria": #O(1)
                    m = int(input("Ingrese el número total de elementos (m): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    resultado = permutacion_sin_repeticion(m) #Complejidad espacial : O(n) # Complejidad temporal : O(n)
                elif tipo_problema == "Permutación con repetición": #O(1)
                    m = int(input("Ingrese el número total de elementos (m): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    elementos_repetidos = list(map(int, input("Ingrese la cantidad de repeticiones de cada elemento separadas por espacios: ").split())) #Complejidad espacial : O(n) # Complejidad temporal : O(n)
                    resultado = permutacion_con_repeticion(m, elementos_repetidos) #Complejidad espacial : O(n) # Complejidad temporal : O(n)
                elif tipo_problema == "Combinación ordinaria": #O(1)
                    m = int(input("Ingrese el número total de elementos (m): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    n = int(input("Ingrese el número de elementos a seleccionar (n): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    resultado = combinacion_sin_repeticion(m, n) #Complejidad espacial : O(n) # Complejidad temporal : O(n)
                elif tipo_problema == "Combinación con repetición": #O(1)
                    m = int(input("Ingrese el número total de elementos (m): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    n = int(input("Ingrese el número de elementos a seleccionar (n): ")) #Complejidad espacial : O(1) # Complejidad temporal : O(1)
                    resultado = combinacion_con_repeticion(m, n) #Complejidad espacial : O(n) # Complejidad temporal : O(n)
                break # se sale del bucle si no se disparó ninguna excepción
            
            except AnswerNotValid:
                print("Error: Alguna de las respuestas ingresada fue inválida ...")
                
            except FloatNotAllowed:
                print("Error: No se permiten valores decimales.")
            
            except NegativeIntegerNotAllowed:
                print("Error: No se permiten números enteros negativos.")
            
            except ValueError:
                 print("Error: Solo se pueden ingresar numeros enteros positivos ...")
                 
            except Exception as e:
                print("Error:", e)

        print (" Se debe responder n ó s")
            
    print("El resultado es:", resultado) #O(1)

if __name__ == "__main__": 
    main() 

if __name__ == "__main__": 
    main() 
