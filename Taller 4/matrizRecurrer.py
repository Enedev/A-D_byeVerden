
def matrixMove(m):
    if not m:
        raise ValueError("Matrix is empty.")

    n = len(m)
    if any(len(row) != n for row in m):
        raise ValueError("Matrix is not square.")

    if any(None in row for row in m):
        raise ValueError("Matrix contains empty values.")

    if any(isinstance(val, str) for row in m for val in row):
        raise ValueError("Matrix contains string values.")

    last_element = m[-1][-1]

    def pathtoNn(row, col, p):
        if row == n - 1 and col == n - 1:
            return p

        if row == n - 1:
            p.append(m[row][col])
            return pathtoNn(row, col + 1, p)

        if col == n - 1:
            p.append(m[row][col])
            return pathtoNn(row + 1, col, p)

        down = pathtoNn(row + 1, col, p.copy())
        down.append(m[row][col])

        right = pathtoNn(row, col + 1, p.copy())
        right.append(m[row][col])

        if m[row + 1][col] > m[row][col + 1]:
            return down
        else:
            return right

    return pathtoNn(0, 0, [last_element])


matrix = [[1, 2, 3, 4],
          [2, 4, 6, 5],
          [5, 6, 8, 5],
          [5, 3, 6, 2]]

try:
    result = matrixMove(matrix)
    result.reverse()
    print(result)
except ValueError as e:
    print(e)

    
        

