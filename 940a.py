n, d = map(int, input().split())
p = list(map(int, input().split()))
res = n- 1
p.sort()

for i in range(n):
    for j in range(i, n):
        if p[j] - p[i] > d:
            continue # set xoa ko hop le
        res = min(res, n -(j-i +1))  # xoa tat ca cac thang ko nam giua 

print(res)


