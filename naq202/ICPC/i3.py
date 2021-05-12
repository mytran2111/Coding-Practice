# use triangle inqualities
def is_triangle(a, b, c):
    val = 0
    val += a + b > c
    val += a + c > b
    val += b + c > a
    return val == 3


n = int(input())

lengths = []

for _ in range(n):
    lengths.append(int(input()))

# brute force try all combos
triangles = 0


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            if is_triangle(lengths[i], lengths[j], lengths[k]):
                print("triangle: {} {} {}".format(lengths[i], lengths[j], lengths[k]))
                triangles += 1

print(triangles)
