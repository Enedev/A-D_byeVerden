def suma_digitos(numero):
    suma = 0
    while numero > 0: # O(n)
        ultimo_digito = numero % 10 # O(1)
        suma += ultimo_digito # O(1)
        numero //= 10 # O(1)
    return suma # O(1)
try:
    numero_entero = int(input("Ingresa un número entero: ")) # O(1)
    resultado = suma_digitos(numero_entero)
    print(f"La suma de los dígitos de {numero_entero} es: {resultado}") # O(1)
except ValueError:
    print("Error: Debes ingresar un número entero.") # O(1)
