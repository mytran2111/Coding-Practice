n = int(input())
grades = list(map(int, input().split()))
grades.sort()
av_grade = sum(grades)/n
need = True 
change = 0 
if av_grade >= 4.5:
    av_grade = 5
if av_grade == 5:
    print(0)
    need = False
if need:
    for i in range(n):
        # print(grades)
        if sum(grades)/n < 4.5:
            # print(i)
            rem = sum(grades) - grades[i]
            if 4.5 *n - rem > grades[i] and grades[i] != 5:
                grades[i] = 5
                change += 1
    print(change)
