n = int(input())
ids = list(map(int, input().split()))

ids.sort()

# create a list counting occurence
ids = [ids.count(x) for x in {*ids}-{0}]
if max(ids+[0]) > 2 :
	print(-1)
else:
	print(ids.count(2))
    # print pair with only two occurence
