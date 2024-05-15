class MatrizNoCuadradaError(Exception):
    def __init__(self, message="La matriz no es cuadrada"):
        self.message = message
        super().__init__(self.message)

def max_path_sum(matrix, cache=None):
    rows, cols = len(matrix), len(matrix[0])
    if rows != cols:
        raise MatrizNoCuadradaError("La matriz no es cuadrada")

    n = len(matrix)

    # se crea el cache si no está
    if cache is None:
        cache = {}

    def dfs(r, c):
        if r == n:
            return 0
        if (r, c) in cache:
            return cache[(r, c)]

        left = dfs(r + 1, c - 1) if c > 0 else 0
        up = dfs(r + 1, c)
        right = dfs(r + 1, c + 1) if c < n - 1 else 0

        cache[(r, c)] = matrix[r][c] + max(left, up, right)
        return cache[(r, c)]

    # Iniciamos la recursión desde la primera fila
    max_sum = float('-inf')
    for i in range(n):
        max_sum = max(max_sum, dfs(0, i))

    return max_sum

# Ejemplos
matrix1 = [[348, 391], [618, 193]]
print(max_path_sum(matrix1))  # Debe imprimir 1009

matrix1_1 = [[348, 391], [193, 618]]
print(max_path_sum(matrix1_1))  # Debe imprimir 1009

matrix3 = [[0, 0], [2, 2]]
print(max_path_sum(matrix3))  # Debe imprimir 2

matrix2 = [[2, 2, 2], [1, 2, 100], [1, 2, 0]]
print(max_path_sum(matrix2))  # Debe imprimir 104




