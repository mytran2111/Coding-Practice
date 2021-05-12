n = int(input())

chocolates = list(map(int, input().split()))
ans = chocolates[n-1]
sums = chocolates[n-1]
i = n-2
while i >= 0: 
    if chocolates[i] >= sums:
        sums -= 1
        ans += sums
        i -= 1
    
    else:
        sums = chocolates[i]
        ans += sums
        i -= 1
    
    if sums == 0:
        break

print(ans)