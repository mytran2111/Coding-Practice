n = int(input())
temps = list(map(int, input().split()))
ans = 0
for i in range(n):
    if temps[i] < 0:
        ans += 1

print(ans)