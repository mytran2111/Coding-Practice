from math import floor
h,m = map(int, input().split(":"))
minute = int(input())
x = h*60 + m + minute
h2 = floor(x/60) % 24
m2 = x % 60
ans = ''
if h2 < 10:
  ans += '0'+str(h2)
else:
  ans += str(h2)
ans += ':'
if m2 < 10:
  ans += '0' +str(m2)

else:
  ans += str(m2)
print(ans)
