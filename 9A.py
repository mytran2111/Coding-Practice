from fractions import Fraction
y, w  = map(int, input().split())

roll = max(y,w)

need = 6 - roll + 1


result = str(need) + "/" + str(6)

#ans = str(result[0]) + '/' + str(result[1]) 
if result == '2/6':
    print('1/3')
elif result == '3/6':
    print('1/2')
elif result == '4/6':
    print('2/3')
elif result == '6/6':
    print('1/1')
else:
    print(result)