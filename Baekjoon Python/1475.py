import sys

set_num = 1
six_or_nine = 0
sets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def addSets(s_n, s):
    s_n += 1
    s = [i+1 for i in sets]
    return s_n, s
    
N = list(sys.stdin.readline().rstrip())

for i in N:
    now = int(i)
    if sets[now]==0 and now==6 and sets[9]>0:
        sets[9]-=1
    elif sets[now]==0 and now==9 and sets[6]>0:
        sets[6]-=1
    elif sets[now]==0:
        set_num, sets = addSets(set_num, sets)
        sets[now] -= 1
    else:
        sets[now] -= 1
print(set_num)
