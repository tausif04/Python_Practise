def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                left_diagonal += arr[i][j]
            if i + j == len(arr) - 1:
                right_diagonal += arr[i][j]

    return abs(left_diagonal - right_diagonal)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
# left_diagonal = 0