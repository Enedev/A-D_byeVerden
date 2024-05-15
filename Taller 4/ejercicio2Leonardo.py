# Aquí van las excepciones
class MatrizNoCuadradaError(Exception):
    def __init__(self, message="La matriz no es cuadrada"):
        self.message = message
        super().__init__(self.message)
        
# Aquí va la función
def max_path_sum(matrix):

    # manejo de excepción : La matriz debe ser NxN
    rows, cols = len(matrix), len(matrix[0])
    if rows != cols:
        raise MatrizNoCuadradaError("La matriz no es cuadrada")
    
    # n = rows = cols (da igual)
    n = len(matrix)

    #dp debe tener las mismas dimensiones que la matrix 
    dp = [[0] * n for _ in range(n)]

    # se inicializa la primera fila de dp con los valores de la matriz
    for i in range(n):
        dp[0][i] = matrix[0][i]

    # Iteramos a través del resto de las filas (sumando y buscando la suma mayor)
    for r in range(1, n):
        for c in range(n):
            # Consideramos los tres movimientos posibles (desde la perspectiva del de abajo)
            left = dp[r - 1][c - 1] if c > 0 else 0
            up = dp[r - 1][c]
            right = dp[r - 1][c + 1] if c < n - 1 else 0

            # Actualizamos la celda actual con la suma máxima
            dp[r][c] = matrix[r][c] + max(left, up, right)

    # Encontramos la suma máxima en la última fila y ese es el resultao
    return max(dp[-1])


matrix1 = [[348, 391], [618, 193]]
print(max_path_sum(matrix1))  # Debe imprimir 1009

matrix1_1 = [[348, 391], [193, 618]]
print(max_path_sum(matrix1_1))  # Debe imprimir 1009

matrix3 = [[0, 0], [2, 2]]
print(max_path_sum(matrix3)) # Debe imprimir 2

matrix2 = [[2, 2, 2], [1, 2, 100], [1, 2, 0]]
print(max_path_sum(matrix2)) # Debe imprimir 104




