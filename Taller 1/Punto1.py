#Dado las dimensiones de una matriz cuadrada, mostrar los
#índices de la matriz en forma de zig-zag empezando por la
#posición[n][n].

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = 3
columns = 3

solution = [[] for i in range(rows + columns - 1)] # This list is used to store the extracted diagonal elements based on their sum (i + j) # O(n) # O(n) 

start_row = 2
start_column = 2 

for i in range(start_row, -1, -1): # O(n)
    for j in range(i if i == start_row else columns - 1, -1, -1):  # Fixed the starting point for j # O(n)
        sum = i + j
        solution[sum].insert(0, matrix[i][j])  # O(1)    

for i in solution[::-1]:  # O(n)
    for j in i: # O(n)
        # Complejidad Temporal: O(1)
        print(j, end=" ") # O(1)

