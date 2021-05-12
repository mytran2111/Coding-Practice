import math
n = int(input())

for i in range(n):
    x = int(input())
    print(math.factorial(x)%10)