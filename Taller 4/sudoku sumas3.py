class ValorFueraDeRango(Exception):
    def _init_(self, msg) -> None:
        self.msg = msg

n= 20
def sudokuSumas(matrix, totalSum):
    #Si no hay mas 0, retorna la matriz final
    if not any(0 in row for row in matrix):
        return matrix

    #Recorrer la matriz por filas
    for i in range(len(matrix)):
        #Si solo hay un cero en la fila
        if len([x for x in matrix[i] if x==0]) == 1:

            for j in range(len(matrix[i])):
                # En la posicion donde hay un 0
                if matrix[i][j] == 0:
                    if totalSum - sum(matrix[i]) > n:
                        raise ValorFueraDeRango(f"El sudoku solo permite valores entre 1 y {n}")
                    #Al resultado se le resta los otros numeros que estén en la fila
                    matrix[i][j] = totalSum - sum(matrix[i])

    #Recorrer la matriz por columnas
    for i in range(len(matrix)):
        suma = 0
        #Contar el numero de ceros
        cont = 0
        for j in range(len(matrix)):
            suma += matrix[j][i]
            if matrix[j][i] == 0:
                row=j
                cont += 1
        #Si solo hay un cero, al resultado se le resta los otros numeros que estén en la columna
        if cont == 1:
            if totalSum - suma > n:
                raise ValorFueraDeRango(f"El sudoku solo permite valores entre 1 y {n}")
            matrix[row][i] = totalSum - suma

    return sudokuSumas(matrix, totalSum)


try:
    for i in sudokuSumas([[5, 0, 2],
                          [8, 5, 0],
                          [0, 2, 0]] , 14):
        print(i)
    print(" ")
    for i in sudokuSumas([[3, 6, 7],
                          [0, 7, 0],
                          [8, 0, 5]] , 16):
        print(i)
    print(" ")
    # for i in sudokuSumas([[3, 6, 7],
    #                       [0, 7, 0],
    #                       [8, 2, 5]] , 50):
    #     print(i)
except ValorFueraDeRango as e:
    print(e.msg)
except:
    print("No se puede realizar el sudoku con los valores ingresados")
