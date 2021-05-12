n, c = map(int, input().split())
w = list()
ans = 0
for i in range(n):
    j = int(input())
    w.append(j)
index = 0
w.sort(reverse=True)

sums = {0}
for elem in w:
    sums.update({sum_ + elem for sum_ in sums if sum_ + elem < c})

sums.discard(0)
need = True
for i in sums:
    for j in w:
        if i == j:
            continue
        if i - j in w:
            ans = i
            need = False
            print(ans)
            exit(0)   
if need:
    ans = max(sums)        
print(ans)