from math import sqrt
n = int(input())

def findPrime(x):
    for i in range(2,int(sqrt(x)) + 1):
        if x % i == 0:
            x+=1
            x = findPrime(x)
            return x
    return x
for i in range(n):
    d = int(input())
    a = findPrime(d+1)
    b = findPrime(d+a)
    print(a*b)