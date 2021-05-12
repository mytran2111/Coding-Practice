n = int(input())

chips = list(map(int, input().split()))
cnto = 0
for i in range(n):
  cnto += chips[i] & 1

print(min(cnto, n-cnto))