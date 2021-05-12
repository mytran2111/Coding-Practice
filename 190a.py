n, m = map(int, input().split())

if n == 0:
    if m == 0:
        print('0 0')
    else:
        print('Impossible')

else:
    if m == 0:
        print(str(n) + ' ' +str(n))
    else:
        print(str(max(n,m)) + ' ' + str(n + m - 1))
    