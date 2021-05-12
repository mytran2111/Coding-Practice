n, q = map(int, input().split())

wealth = [0]*n
time = [0]*n
rts = 0
Gx = 0 
for x in range(1,q+1):    
    list_input = input().split()
    if list_input[0] == 'SET':
        wealth[int(list_input[1])-1] = int(list_input[2])
        time[int(list_input[1])-1] = x
        continue
    if list_input[0] == 'RESTART':
        Gx = int(list_input[1])
        rts = x
        continue
    if list_input[0] == 'PRINT':
        if time[int(list_input[1])-1] < rts:
            print(Gx)
        else:
            print(wealth[int(list_input[1])-1])
        continue
    
