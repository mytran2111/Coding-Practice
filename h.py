# Java BigInterger class or input() in Python3 will fail this question.
#the reason is because: standard object stores numbers not in decimal sysstem and need a lot of time to 
# converst numbers from decimal system hence they are working in O(n^2)

#Idea; treat it as string, as teh leading zeros to the shorter one until the numbers will be of same length
# then compare them alphabetically

a = input()
b = input()

l = max(len(a), len(b))
da = len(a) - l
db = len(b) - l

for i in range(l):
    start_a = '0'
    if da + i >= 0:
        start_a = a[da+i]

    start_b = '0'
    if db + i >= 0:
        start_b = b[db + i]

    if start_a < start_b:
        print('<')
        exit(0)
    else:
        if start_a > start_b:
            print('>')
            exit(0)
        
print('=')   