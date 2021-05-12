tests = int(input())
ans = []
for test in range(tests):
    n, s, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(k+1):
        if s -i >= 1 and (s-i not in a): 
            ans.append(i)
            break
        if s + i <= n and (s+i not in a):
            ans.append(i)
            break
    else:
         assert(False) 

print(*ans, end = ' ') 