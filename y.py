n = int(input())

x = 1
y = 2
work = True 
for i in range(n):
    w = int(input())
    if w == x or w == y:
        y = 6 - x -y # update the third player
        x = w
    else:
        work = False

if work:
    print('YES')
else:
    print('NO')