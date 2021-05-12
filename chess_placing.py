n = int(input())
chess = list(map(int, input().split()))

move1 = 0
move2 = 0

chess.sort()

for i in range(len(chess)):
    move1 += abs(chess[i] - (i * 2 + 1))
    move2 += abs(chess[i] - (i * 2 + 2))

print(min(move1, move2))