#Punto 2 (2.0): Dado un número entero N que representa el número de pares de paréntesis, 
# la tarea es generar todas las combinaciones de paréntesis bien formados (equilibrados).

def generateParenthesis(N):
    def generate(p, left, right, parens=[]):
        if left:
            generate(p + '(', left-1, right)
        if right > left:
            generate(p + ')', left, right-1)
        if not right:
            parens += p,
        return parens

    return generate('', N, N)

# Ejemplo de uso
N = 3
print(generateParenthesis(N))
    
