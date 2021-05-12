def overlap(l):
    sorted(l)
    result = list()
    for i in range(len(l)):
        if l[i][1] >= l[i+1][1]:
            # merge the list 
            result.append([l[i][0], l[i+1][1]])
    return result

    if __name__ == '__main__':

        l = [[1,3],[2,6],[8,10],[15,18]]
        print(overlap(l))