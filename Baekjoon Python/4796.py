import sys

L = [[5,8,20],[5,8,17],[0,0,0]]
'''
for line in sys.stdin:
    L.append(list(map(int, line.strip().split())))
'''
L.pop()
for i in range(len(L)):
    days = (L[i][2]//L[i][1])*L[i][0]
    left = L[i][2] - (L[i][2]//L[i][1])*L[i][1]
    days += min(left, L[i][0])
    print("Case %d: %d" %(i+1, days))
