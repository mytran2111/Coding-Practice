
sum_white = 0
sum_black = 0

white = {'Q':9, 'R': 5, 'B':3, 'N':3, 'P':1, 'K':0}
black = {'q':9, 'r':5, 'b':3, 'n':3, 'p':1, 'k':0}

for i in range(8):
    line = input()
    for j in range(8): 
        if line[j].isupper():
            sum_white += white[line[j]]
        if line[j].islower():
            sum_black += black[line[j]]

if sum_white < sum_black:
    print('Black')
elif sum_white > sum_black:
    print('White')
else:
    print('Draw')