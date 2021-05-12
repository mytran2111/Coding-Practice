import math
h, v = map(int, input().split())
print((int(h//math.sin(math.radians(v))) + 1))
