n = int(input())
candies = list(map(int, input().split()))
num = 0 
odd = 0
even = 0 
evenPref = 0
oddPref = 0 
for i in range(n):
    if not(i &1):
        even += candies[i]
    else:
        odd += candies[i]

for i in range(n):
    if not(i &1):
        even -= candies[i]
    else:
        odd -= candies[i]
    if evenPref + odd == oddPref + even:
        num += 1
    if not(i & 1):
        evenPref += candies[i]
    else:
        oddPref += candies[i] 
print(num)