import sys
import string

temp = []
N = sys.stdin.readline().rstrip()
L = list(map(int, list(N)))
if (0 not in L) or (sum(L)%3!=0):
    print(-1)
else:
    L.remove(0)
    L.sort(reverse=True)
    L.append(0)
    '''
    num = L.count(0)
    if num >= 1:
        temp.append([L[num]])
        temp.append(L[0:num])
        temp.append(L[num+1:])
    else:
        temp.append(L)
    temp.append([0])
    temp2 = sum(temp, [])
    answer = ''.join(str(i) for i in temp2)
    '''
    answer = ''.join(str(i) for i in L)
    print(answer)
