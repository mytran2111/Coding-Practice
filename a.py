t = int(input())

for i in range(t):
    a,b,c = map(int, input().split())
    result = 0
    if(a<b):
        a, b = b,a
    if( a< c):
        a,c = c, a
    if (b<c):
        b,c = c,b
    if(a):
        result += 1
        a -= 1
    if(b):
        result += 1
        b -= 1
    if(c):
        result += 1
        c -= 1
    if( a and b):
        result += 1
        a -= 1
        b -= 1
    if( a and c):
        result += 1
        a -= 1
        c -= 1 
    if( c and b):
        result += 1
        c -= 1
        b -= 1
    if( a and b and c):
        result += 1
        a -= 1
        b -= 1
        c -= 1
    
    print(result)