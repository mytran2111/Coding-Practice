s, v1, v2, t1, t2 = map(int, input().split())

time_1 = s * v1 + 2 * t1
time_2 = s * v2 + 2 * t2

if time_1 < time_2:
    print('First')
elif time_1 > time_2:
    print('Second')
else:
    print('Friendship')    