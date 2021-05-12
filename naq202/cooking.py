n = int(input())

minutes = [n for _ in range(0, 1001)]

first_boil = 100
last_boil = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    a = arr[0]
    b = arr[1]

    for i in range(a, b+1):
        minutes[i] -= 1

    if a < first_boil:
        first_boil = a

    if b > last_boil:
        last_boil = b


printed = False
for j in range(first_boil, last_boil+1):
    if minutes[j] == 0:
        print("gunilla has a point")
        printed = True
        break

if printed is False:
    print("edward is right")


