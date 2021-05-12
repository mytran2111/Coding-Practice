n = int(input())
l = list()
for i in range(n):
    a = int(input())
    l.append(a)

for i in range(n):
    if l[i] % 2 == 0:
        print(str(l[i]) + ' is even')
    else:
        print(str(l[i]) + ' is odd')