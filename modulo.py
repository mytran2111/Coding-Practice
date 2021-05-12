l = list(map(str, input().split()))
need = True
for i in l:
    if l.count(i) != 1:
        print('no')
        need = False
if need:
    print('yes')
