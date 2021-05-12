n = int(input())

first = input()
second = input()
right = True
for i in range(len(first)):
    if n % 2 == 0:
        if first[i] != second[i]:
            print('Deletion failed')
            right = False
            break
    else:
        if(abs(int(first[i]) -int(second[i]))) != 1:
            print('Deletion failed')
            right = False
            break

if right:
    print('Deletion succeeded')