n, m = map(int, input().split())
# answer list of n students
s = list()

for i in range(n):
  s.append(input())

# points of m questions
a = list(map(int, input().split()))

# count the different in their answer
cnt = list()
ans = 0
for i in range(m):
  for j in range(n):
    cnt[i][s[j][i] - 'A']+=1
  for j in range(5):
    ma = max(ma, cnt[i][j])
  ans += ma*a[i]

print(ans)