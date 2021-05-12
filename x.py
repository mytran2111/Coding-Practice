n = int(input())
doors = list(map(int, input().split()))
left = doors.count(0)
right = doors.count(1)
k = 0
for i in range(n):

    if left == 0 or right == 0:
        break
    k += 1
    if doors[i] == 0:
        left -= 1
    else:
        right -= 1

print(k)