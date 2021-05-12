
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = int(input())

shelf_a = (sum(a) + 5 -1) // 5
shelf_b = (sum(b) + 10 -1 )// 10


if (shelf_a+shelf_b) <= n:
    print('YES')
else:
    print('NO')
