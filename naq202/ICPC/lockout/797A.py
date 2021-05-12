import math
n, k = map(int, input().split())

result = []

while (n%2 == 0):
    result.append(2)
    n = n//2

# n will be odd at this point 
for i in range(3,int(math.sqrt(n))+1, 2):
    while (n%i == 0):
        result.append(i)
        n = n//i

# check if n is prime >  2
if (n>2):
    result.append(n)


if len(result) < k:
    print("-1")
    exit(0)

for i in range(k-1):
    print(result[i], end=' ')

ans = 1
for i in range(k-1, len(result)):
    ans *= int(result[i])
    
print(ans)
