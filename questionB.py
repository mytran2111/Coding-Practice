from math import sqrt
cx, cy, n = map(int, input().split())
radius = []

for i in range(n):
    x,y, r = map(int, input().split())
    ri = sqrt((cx - x)**2 + (cy-y)**2) - r
    d = sqrt((cx - x)**2 + (cy-y)**2) 
    radius.append(ri)
    
radius.sort()

print(max(0,int(radius[2])))

