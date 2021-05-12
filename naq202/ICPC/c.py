from sys import stdin 

n, k = [int(x) for x in stdin.readline().split()]
arr = []
score = k

for i in range(n):
    inp = stdin.readline()
    arr.append(inp)

if n == 1:
    print(k)
    exit(0)

def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count

min_hams = []
for i in range(n):
    key_set = arr[i]
    hams = []
    for ans in arr:
        if not ans == key_set:
            hams.append(hammingDist(key_set, ans))
    if len(hams) == 0:
        print(k)
        exit(0)
    min_hams.append(max(hams))
    
print(score - min(min_hams))

