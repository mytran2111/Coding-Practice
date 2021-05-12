n = int(input())

skills = list(map(int, input().split()))

skills = [0] + skills
prog = []
maths =[]
pe =[]
skill_dict = {'prog': 0, "maths": 0, 'pe':0}
team = 0

for i in range(n+1):
    if skills[i] == 1:
        skill_dict['prog'] += 1
        prog.append(i)
    if skills[i] == 2:
        skill_dict['maths'] += 1
        maths.append(i)
    if skills[i] == 3:
        skill_dict['pe'] += 1
        pe.append(i)

ans = min(len(prog), len(maths), len(pe))
print(ans)

for i in range(ans):
    print(prog[i], maths[i], pe[i])
    