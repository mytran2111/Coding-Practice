start = list(map(int, input().split(':')))
end = list(map(int, input().split(":")))

ans = ''

t1 = start[0] * 60 + start[1]
t2 = end[0]*60 + end[1]

t3 = (t1 + t2)/2

hour = int(t3 //60)
minute = int(t3 % 60)

if hour < 10:
    hour = '0' + str(hour)

if minute < 10:
    minute = '0' + str(minute)
ans = '' + str(hour) + ':' + str(minute)
print(ans)