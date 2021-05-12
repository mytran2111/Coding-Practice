n, m, k = map(int, input().split())
move = 1
l = [[False] * 1001] * 1001
for i in range(1,k+1):
  a, b = map(int, input().split())
  a = a- 1
  b = b-1 
  l[a][b] = True
  for x in range(-1,2,2):
    for y in range(-1,2,2):
      if a+x < 0 or a+x > n:
        continue
      if b+y < 0 or b+y > m:
        continue
      if (l[a+x][b+y] and l[a+x][b] and l[a][b+y]):
        move = i
print(move)

