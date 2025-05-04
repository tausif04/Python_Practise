def input_matrix(rows, cols, matrix_name):
    matrix = []
    print(f"Enter the elements of matrix {matrix_name} ({rows}x{cols}):")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Each row must have exactly {cols} elements.")
        matrix.append(row)
    return matrix
def multiply_matrices(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    cols_matrix2 = len(matrix2[0])

    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result



rows_matrix1 = int(input("Enter the number of rows for matrix1: "))
cols_matrix1 = int(input("Enter the number of columns for matrix1: "))

rows_matrix2 = int(input("Enter the number of rows for matrix2: "))
cols_matrix2 = int(input("Enter the number of columns for matrix2: "))

if cols_matrix1 != rows_matrix2:
        print("Matrix multiplication is not possible. The number of columns in matrix1 must be equal to the number of rows in matrix2.")
else:

        matrix1 = input_matrix(rows_matrix1, cols_matrix1, "Matrix 1")
        matrix2 = input_matrix(rows_matrix2, cols_matrix2, "Matrix 2")


        result_matrix = multiply_matrices(matrix1, matrix2)
        print("\nResulting Matrix after multiplication:")
        for row in result_matrix:
            print(row)
