from math import *

n = int(input())
x = []
y = []
r = []
for i in range(n): 
    xa, ya, ra = map(int, input().split())
    x.append(xa)
    y.append(ya)
    r.append(ra)
def is_between(gamma, alpha, beta):
    if alpha < -pi + 1e-4 and beta > pi - 1e-4:
        return True
    return (gamma - alpha) % (2 * pi) < (beta - alpha) % (2 * pi)
ans = 0
def length(u, v):
    if u < -pi + 1e-4 and v > pi - 1e-4:
        return v - u
    else:
        return (v - u) % (2 * pi)
for i in range(n):
    flag = False
    start = [-pi]
    end = [pi]
    for j in range(i + 1, n):
        x1, y1, r1 = (x[j]- x[i]) / r[i], (y[j] - y[i]) / r[i], r[j] / r[i]
        d = sqrt(x1 ** 2 + y1 ** 2)
        if d >= 1 + r1 or d <= 1 - r1:
            d_start = pi
            d_end = -pi
        elif d <= r1 - 1:
            flag = True
            continue
        else:
            a = (1 - r1 ** 2 + d ** 2) / (2 * d)
            h = sqrt(1 - a ** 2)
            x2 = a * x1 / d
            y2 = a * y1 / d
            x3 = x2 + h * y1 / d
            x4 = x2 - h * y1 / d
            y3 = y2 + h * x1 / d
            y4 = y2 - h * x1 / d
            alpha = atan2(y3, x3)
            beta = atan2(y4, x4)
            gamma = atan2(y1, x1)
            d_start, d_end = alpha, beta
            if not is_between(gamma, alpha, beta):
                d_start, d_end = d_end, d_start
        for k in range(len(start)):
            u, v = start[k], end[k]
            if is_between(d_start, u, v):
                if is_between(d_end, u, v):
                    if is_between(d_end, u, d_start):
                        end[k] = d_start
                        start[k] = d_end
                    else:
                        start[k], end[k] = u, d_start
                        start += [d_end]
                        end += [v]
                else:
                    end[k] = d_start
            else:
                if is_between(d_end, u, v):
                    start[k] = d_end
    if not flag:
        ans += r[i] * sum(length(start[k], end[k]) for k in range(len(end)))
print(ans)
        
        
        
        
