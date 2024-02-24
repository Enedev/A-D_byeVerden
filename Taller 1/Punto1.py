matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = 3
columns = 3

solution = [[] for i in range(rows + columns - 1)] # This list is used to store the extracted diagonal elements based on their sum (i + j)

start_row = 2  
start_column = 2 

for i in range(start_row, -1, -1):
    for j in range(i if i == start_row else columns - 1, -1, -1):  # Fixed the starting point for j
        sum = i + j
        solution[sum].insert(0, matrix[i][j])

for i in solution[::-1]:
    for j in i:
        print(j, end=" ")

