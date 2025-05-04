matrix = [
    [3, 8, 2],
    [10, 6, 7],
    [4, 9, 5]
]

def find_max(matrix):
    max_value = matrix[0][0]
    max_position = (0, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)

    print(f"The maximum value is {max_value} at position {max_position} (row {max_position[0]}, column {max_position[1]}).")

find_max(matrix)
