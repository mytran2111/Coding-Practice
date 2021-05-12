n = int(input())

p = [0,0] +list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

colors = 1

for i in range(2,n+1):
    if c[i] != c[p[i]]:
        colors += 1

print(colors)
