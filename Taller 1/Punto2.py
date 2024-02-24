def suma_digitos(numero):
    suma = 0
    while numero > 0:
        ultimo_digito = numero % 10
        suma += ultimo_digito
        numero //= 10
    return suma
try:
    numero_entero = int(input("Ingresa un número entero: "))
    resultado = suma_digitos(numero_entero)
    print(f"La suma de los dígitos de {numero_entero} es: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número entero.")
