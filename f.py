n = int(input())

numbers = list(map(int, input().split()))
numbers = [0] + numbers + [1001]
n += 2
ans = 0
clear = 0 

for a in range(n):
    for b in range(a+1,n):
        if (numbers[b] - numbers[a]) == (b-a):
            clear = b-a -1
            ans = max(ans,clear)

print(ans)

