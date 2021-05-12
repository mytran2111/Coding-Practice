word = input()
a = 0
b = 0 
c = 0
stop = False 
for i in range(len(word)-1):
    if ord(word[i]) > ord(word[i+1]):
        stop = True
        break
    if word[i] == 'a':
        a += 1
    if word[i] == 'b':
        b += 1
    if word[i] == 'c':
        c += 1
if word[len(word) - 1] == 'c':
    c += 1
if not stop and a >= 1 and b >= 1 and c >=1 and ((c == a) or (c == b )):
    print('YES')
else:
    print('NO')
