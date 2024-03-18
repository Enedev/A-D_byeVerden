def introduccion_conteo(): #0(1)
    # Función que imprime una introducción al conteo y sus fundamentos.
    print("Es una rama de las matemáticas que se centra en el estudio y el conteo de las diferentes formas en que los objetos pueden ser seleccionados, ordenados o agrupados. Intuitivamente, el conteo es una habilidad fundamental que utilizamos en nuestra vida diaria para resolver problemas como cuántas combinaciones de ropa podemos elegir para vestirnos, cuántas formas diferentes podemos ordenar una lista de canciones en una lista de reproducción o cuántos equipos diferentes pueden formarse a partir de un grupo de personas."
          "El estudio del conteo comienza con la comprensión de conceptos básicos como permutaciones, combinaciones y variaciones, así como la aplicación de principios fundamentales como el principio de multiplicación y el principio de adición.\n")
    #0(1)
    
def definicion_permutacion(): #0(1)
    # Función que define permutaciones y proporciona un ejemplo.
    print("Las permutaciones son arreglos ordenados de elementos. En términos más simples, una permutación es una disposición en la que el orden importa. "
          "Cada permutación representa una forma diferente de organizar los elementos de un conjunto dado.")
    #0(1)
    print("Ejemplo: Supongamos que tenemos tres letras: A, B y C. Las permutaciones de estas letras son ABC, ACB, BAC, BCA, CAB y CBA.\n")
    #0(1)

def definicion_combinacion(): #0(1)
    # Función que define combinaciones y proporciona un ejemplo.
    print("Las combinaciones son selecciones no ordenadas de elementos de un conjunto. En otras palabras, las combinaciones representan agrupaciones en las que el orden de los elementos no importa. "
          "Este concepto es esencial cuando queremos calcular el número de formas en que se pueden seleccionar subconjuntos de elementos de un conjunto más grande.")
    #0(1)
    print("Ejemplo: Si tenemos un conjunto de cinco colores: rojo, azul, verde, amarillo y blanco, y queremos seleccionar tres colores para pintar una bandera, las combinaciones posibles serían rojo, azul y verde, rojo, azul y amarillo, etc.\n")
    #0(1)

def definicion_variacion(): #0(1)
    # Función que define variaciones y proporciona un ejemplo.
    print("Las variaciones son selecciones ordenadas de elementos de un conjunto. A diferencia de las permutaciones, donde se usan todos los elementos, en las variaciones se toma solo un subconjunto de elementos, pero su orden sigue siendo importante.")
    #0(1)
    print("Ejemplo: Si tenemos tres cartas: A, B y C, y queremos formar palabras de dos letras, las variaciones posibles serían AB, BA, AC, CA, BC y CB.\n")
    #0(1)
 
def definicion_principio_aditivo(): #0(1)
    # Función que define el principio aditivo y proporciona un ejemplo.
    print("Es un concepto fundamental en combinatoria que establece que si hay múltiples formas mutuamente excluyentes de realizar un evento o una tarea, entonces el número total de posibilidades es la suma de las formas individuales. En otras palabras, si dos o más eventos no pueden ocurrir simultáneamente, el número total de resultados posibles es la suma de los resultados de cada evento por separado."
          "El principio de adición es esencial en la resolución de problemas de conteo donde las opciones son mutuamente excluyentes, lo que significa que no pueden ocurrir simultáneamente.")
    #0(1)
    print("Ejemplo: Si queremos calcular el número de formas de llegar a una fiesta, podemos sumar el número de formas de llegar en auto, en bicicleta o a pie.\n")
    #0(1)

def definicion_principio_multiplicativo(): #0(1)
    # Función que define el principio multiplicativo y proporciona un ejemplo.
    print("El principio de multiplicación es una regla fundamental en combinatoria que establece que si un experimento o evento puede ocurrir de m maneras diferentes, y otro evento independiente puede ocurrir de n maneras diferentes, entonces el número total de formas en que ambos eventos pueden ocurrir es el producto de m y n."
          "En otras palabras, si tienes m opciones para la primera etapa de un proceso y, independientemente de la elección anterior, tienes n opciones para la segunda etapa, entonces el número total de resultados posibles para todo el proceso es m veces n. Este principio es útil para calcular el número total de arreglos, combinaciones o permutaciones que pueden ocurrir en una secuencia de eventos independientes. "
          "Es fundamental en la resolución de problemas de conteo donde se consideran múltiples opciones en secuencia.")
    #0(1)
    print("Ejemplo: Si tenemos 4 camisas y 3 pantalones, el número total de combinaciones de vestimenta que podemos hacer es 4 (opciones de camisas) multiplicado por 3 (opciones de pantalones), lo que nos da 12 combinaciones en total.\n")
    #0(1)

def situaciones_vida_real(): #0(1)
    # Función que describe las situaciones de la vida real en las que se aplican los conceptos de conteo.
    print("Los conceptos de conteo, permutación, combinación y variación se utilizan en numerosas situaciones de la vida real, como en la planificación de eventos, la elaboración de menús, la creación de contraseñas seguras, el diseño de experimentos, la distribución de premios, entre otros.\n")
    #0(1)

def mostrar_menu():
    # Función principal que muestra un menú de opciones y llama a las funciones correspondientes según la opción seleccionada.
    while True:
        print("Bienvenido al sistema de definiciones de conteo:") #0(1)
        print("1. Introducción al conteo") #0(1)
        print("2. Definición de permutación") #0(1)
        print("3. Definición de combinación") #0(1) 
        print("4. Definición de variación") #0(1)
        print("5. Definición del principio aditivo")    #0(1)
        print("6. Definición del principio multiplicativo") #0(1)
        print("7. Situaciones de la vida real") #0(1)
        print("0. Salir") #0(1)

        opcion = input("Por favor, seleccione una opción: ") #Complejidad temporal: O(1) Complejidad espacial: O(1)

        if opcion == "1": #0(1)
            introduccion_conteo() #0(1)
        elif opcion == "2": #0(1)
            definicion_permutacion() #0(1)
        elif opcion == "3": #0(1)
            definicion_combinacion() #0(1)
        elif opcion == "4": #0(1)
            definicion_variacion() #0(1)
        elif opcion == "5": #0(1)
            definicion_principio_aditivo() #0(1)
        elif opcion == "6": #0(1)
            definicion_principio_multiplicativo() #0(1)
        elif opcion == "7": #0(1)
            situaciones_vida_real() #0(1)
        elif opcion == "0": #0(1)
            print("Gracias por usar el sistema de definiciones de conteo. ¡Hasta luego!") #0(1)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n") #0(1)

# Ejecutar la función para mostrar el menú
mostrar_menu() 
