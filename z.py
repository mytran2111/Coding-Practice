a, b, s = map(int, input().split())

sums = abs(a) + abs(b)
if s >= sums and (s-sums) % 2 == 0:
    print('Yes')
else:
    print('No')

