from math import ceil
n,k = map(int, input().split())
w = [0] + list(map(int, input().split()))
minDay = 0
total = 0
for i in range(1,n+1):
    total += ceil(w[i]/k)
minDay = ceil(total/2)
print(minDay) 

