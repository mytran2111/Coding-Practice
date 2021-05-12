import copy
n, s = map(int, input().split())
cards = list(map(int,input().split()))
copy = copy.deepcopy(cards)
need = True
for i in range(n):
    a = ''
    if cards[i] > 9:

        while copy[i] > 0:
            a += str(copy[i] % 10)
            copy[i] = (copy[i] - copy[i]%10)//10
        if (int(a) not in cards):
            cards.append(int(a))
print(cards)
for i in range(len(cards)):
    if (s - cards[i]) in cards and (cards.index((s-cards[i])) !=i +n and cards.index((s-cards[i])) != i - n  ) :
        need = False
        print('YES')
        break
if need:
    print('NO')

