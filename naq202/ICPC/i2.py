def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def isNotTriange(a):

    # print("trying subset")
    # print(a)

    # for i in range(len(a)):
    #     for j in range(i+1, len(a)):
    #         for k in range(j+1, len(a)):
    #             if not is_triangle(a[i], a[j], a[k]):
    #                 print("fail on {} {} {}".format(a[i], a[j], a[k]))
    #                 return False
    # return True

    # a.sort()
    # for i in range(len(a) - 2):
    #     if ( not is_triangle(a[i], a[i+1], a[i+2])):
    #         return False
    # return True 

    """
    for i in range(len(a) - 2):
        if (a[i] + a[i+1] <= a[i+2]) or (a[i+1] + a[i+2] <= a[i]) or (a[i+2] + a[i] <= a[i+1]):
            return False
    return True

    """
    for i in range(len(a) - 2):
        if (a[i] + a[i+1] <= a[i+2]) or (a[i+1] + a[i+2] <= a[i]) or (a[i+2] + a[i] <= a[i+1]):
            return True
    return False

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
#print(sublists)
for i in sublists:
    if len(i) >= 3 and not isNotTriange(i):
        ans += 1
print(ans)
