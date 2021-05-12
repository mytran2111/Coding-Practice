action = input()
word = input()

key = 'qwertyuiopasdfghjkl;zxcvbnm,./'
result = ''

for i in word: 
    if action == 'L':
        if key.find(i) == len(key):
            result += 'q'
        else:
            result += key[key.find(i) + 1]

    else: 
        result += key[key.find(i) -1]

print(result)