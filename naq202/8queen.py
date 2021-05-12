n = int(input())
arr = list(map(int, input().split()))

# i is starting index of hike
i = 0
# heat is min top temperature starting trip on i
heat = 41

for j in range(n-2):
    hiking_days_max_heat = max(arr[j], arr[j+2])

    if hiking_days_max_heat < heat:
        heat = hiking_days_max_heat
        i = j

print("{} {}".format(i+1, heat))





