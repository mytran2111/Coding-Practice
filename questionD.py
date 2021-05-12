n = int(input())

for i in range(n):
    s = input()
    for j in range(1,len(s)+1):
        mult = len(s)//len(s[:j])
        rem = len(s) % len(s[:j])
        if (s[:j] * mult + s[:rem]) == s:
            print(j)
            break 
