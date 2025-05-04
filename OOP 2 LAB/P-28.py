matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

def sum_of_rows(matrix):
    for index, row in enumerate(matrix):
        row_sum = sum(row)
        print(f"Sum of row {index + 1}: {row_sum}")

sum_of_rows(matrix)
