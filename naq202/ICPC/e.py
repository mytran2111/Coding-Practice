n = int(input())
cards = list(map(int, input().split()))
score = 0
cards.sort()
last = cards[0]
score += last
for i in range(1,n):
    if not last + 1 == cards[i]:
         score += cards[i]
    last = cards[i]

print(score)
