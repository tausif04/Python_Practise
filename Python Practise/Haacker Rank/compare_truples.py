def compareTriplets(a, b):
    ali = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            ali += 1
        elif b[i] > a[i]:
            bob += 1
    return [ali, bob]

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))