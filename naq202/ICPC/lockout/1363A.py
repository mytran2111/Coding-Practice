t = int(input())

for i in range(t):
    n,x = map(int, input().split())
    a = list(map(int,input().split()))
    odd = 0
    even = 0
    for j in range(n):
        if a[j] % 2 == 1:
            odd += 1
        else:
            even += 1
    m = min(even,x-1)
    d= x - m

    if d % 2 == 0:
        d+=1
    if odd >= d and d <= x:
        print("YES")
    else:
        print("NO")