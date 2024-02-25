matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = 3
columns = 3

solution = [[] for i in range(rows + columns - 1)] # This list is used to store the extracted diagonal elements based on their sum (i + j) # O(rows + columns)

start_row = 2  
start_column = 2 

for i in range(start_row, -1, -1): # O(rows)
    for j in range(i if i == start_row else columns - 1, -1, -1):  # Fixed the starting point for j # O(columns - i)
        sum = i + j
        solution[sum].insert(0, matrix[i][j])  # O(1)    

for i in solution[::-1]:  # O(rows + columns)
    for j in i: # O(min(rows, columns))
        print(j, end=" ") # O(1)

