n = int(input())
bus = list(map(int, input().split()))

rep = list()
bus.sort()
count = 0

for i in range(n):
    if i == n- 1:
        if count > 1:
            rep.append(str(bus[n-1-count]) + '-' +str(bus[n-1]))
            count = 0
        elif count == 1:
            rep.append(bus[n-2])
            rep.append(bus[n-1])
            count = 0 
        else:
            rep.append(bus[n-1])

    else:
        if bus[i] + 1 == bus[i+1]:
            count += 1 
            continue
        else:
            if count > 1:
                rep.append(str(bus[i-count]) + '-' + str(bus[i]))
                count = 0
            elif count == 1:
                rep.append(bus[i-1])
                rep.append(bus[i])
                count = 0
            else:
                rep.append(bus[i])

print(*rep, end= ' ')


    