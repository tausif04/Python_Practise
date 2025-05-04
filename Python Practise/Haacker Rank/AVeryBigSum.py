def aVeryBigSum(ar):
    sum=0
    for i in range(len(ar)):
        sum += ar[i]
    return sum


ar=list(map(int, input().rstrip().split()))
result=aVeryBigSum(ar)
print(result)