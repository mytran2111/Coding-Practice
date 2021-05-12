n = int(input())

for i in range(n):
    s = set(input().lower())
    missing = []
    for j in range(ord('a'), ord('z') +1):
        if chr(j) not in s:
            missing.append(chr(j))

    if len(missing) == 0:
        print('pangram')
    else:
        print('missing ' + ''.join(missing)) 

