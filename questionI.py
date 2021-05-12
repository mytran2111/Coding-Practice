n, m = map(int, input().split())

indegree = [0]*n

for i in range(m):
    l = input().split()
    indegree[l[1]-1] += 1

for i in range(n):
    if indegree[i] == 0:
       print(i) 

