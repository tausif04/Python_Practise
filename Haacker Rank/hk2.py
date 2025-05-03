n=int(input())
a=list(map(int, input().split()))

a.sort(reverse=True)

for i in a:
    if i < a[0]:
        print(i)
        break