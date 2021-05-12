def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l

print(bubble_sort([1,4,2,3]))

def insertion_sort(l):
    for 