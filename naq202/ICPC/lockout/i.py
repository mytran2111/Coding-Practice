def create(n):
    h = []
    for i in range(1,n+1):
        h.append(i)
    return h

def op2(n,p):
    if p < n -1 :
        return []
    l = []
    t = 0
    c = 1

    for i in range(n-1,0,-1):
        c += 1

        if (t+c+i-1 >= p):
            r = p -t -i +1
            l.append(r)
            for k in range(i-1):
               l.append(1)
            t = p
            break
        t += c
        l.append(c)

    if t < p:
        return []
    return l

def op1(h,h1):
    length = len(h1)
    for i in range(length):
        t = len(h) - (i+2)
        s = t + h1[i]
        h = h[:t] + list(reversed(h[t:s])) + h[s:] 
    return h
    

def solve():
    inp = input().split()
    n = int(inp[0])
    c = int(inp[1])
    h = create(n)
    h1 = op2(n,c)
    h = op1(h,h1)
    print(h)
    ans = ' '

    if h1:
        for item in h:
            ans += str(item) + ' '
    else:
        ans = 'Impossible'
    print("Case #" + str(i+1) +": " + str(ans)) 
    

for i in range(int(input())):
    solve()

    # print("Case #" + str(i+1) +": " + str(ans))

# t = int(input())
# def reverse(i,j,l):
#     x = i
#     y = j
    
#     while x <= y:
#         l[x], l[y] = l[y], l[x]
#         x+= 1
#         y -= 1
# for k in range(t):
#     n = int(input())
#     l = list(map(int, input().split()))
#     cost = 0
    
#     for i in range(n-1):
#         minIndex = n-1
#         minTerm = 2147483647
        
#         for j in range(n-1,i-1,-1):
#             if l[j] < minTerm:
#                 minTerm = l[j]
#                 minIndex = j
                
#         reverse(i, minIndex,l)
#         cost += minIndex -i + 1
        
#     print("Case #" + str(k+1) + ':' + ' ' + str(cost))