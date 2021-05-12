def isTriange(a):
    for i in range(len(a) - 2):
        if (a[i] + a[i+1] <= a[i+2]) or (a[i+1] + a[i+2] <= a[i]) or (a[i+2] + a[i] <= a[i+1]):
            return False
    return True

def sublist(l):
    base = []   
    lists = [base] 
    for i in range(len(l)): 
        orig = lists[:] 
        new = l[i] 
        for j in range(len(lists)): 
            lists[j] = lists[j] + [new] 
        lists = orig + lists 
          
    return lists 
n = int(input())
l = list()

for i in range(n):
    j = int(input())
    l.append(j)

l.sort()
ans = 0

sublists = sublist(l)
print(sublists)
for i in sublists:
    if len(i) >= 3 and isTriange(i):
        ans += 1
print(ans) 

