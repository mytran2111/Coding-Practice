def recursion(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return recursion(n-1) + recursion(n-2)

print(recursion(50))