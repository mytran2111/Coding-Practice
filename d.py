from math import sqrt
b = int(input())

i = 1
total = 0

while i * i <= b:
    if b % i == 0:
        total += 2
    i += 1 

s = round(sqrt(b))
if b == s * s:
    total -= 1

print(total)