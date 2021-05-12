a, b = map(int, input().split())

x = 1

while(True):
    if x > a:
        print("Vladik")
        exit(0)
    else:
        a -= x
        x+=1
    if x> b:
        print("Valera")
        exit(0)
    else:
        b -= x
        x+=1    