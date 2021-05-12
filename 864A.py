n = int(input())
l = []
for i in range(n):
    s = int(input())
    l.append(s)

l.sort()
need = True

if l[0] != l[(n-1)//2]:
    print('NO')
    need = False
elif l[(n-1)//2 + 1] != l[n-1]:
    print('NO')
    need = False
elif l[0] == l[n-1]:
    print('NO')
    need = False
else:
    print('YES')
    print(l[0], end=' ')
    print(l[n-1])