test = int(input())
answer = []

for i in range(test):
    n = int(input())
    numbers = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if numbers[i] == 0:
            numbers[i] = 1
            ans += 1
    if sum(numbers) == 0:
        ans += 1
    answer.append(ans)

print(*answer, end = ' ')

