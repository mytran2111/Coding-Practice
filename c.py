n = int(input())

s = int(input())
ans = []

digit = 0

while s > 0:
    if s % 10 == 0:
        digit = 0
        if s % 100 != 0:
            ans.append(digit)
            s = s/10
        else:
            ans.append(0)
            s = s//100
    else: 
        digit += 1
        s = (s - 1)/10
        
str_ans = ''

for i in range(len(ans) -1, -1, -1):
    str_ans += str(n[i])

print(int(str_ans))