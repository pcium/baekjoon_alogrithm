import sys

N = int(sys.stdin.readline())
WAY = ['INCREASING', 'DECREASING', 'NEITHER']
NAMES = []
for i in range(N):
    NAMES.append(sys.stdin.readline().rstrip())
names = NAMES[:]
names.sort()
if NAMES == names:
    print(WAY[0])
else:
    names.sort(reverse=True)
    if NAMES == names:
        print(WAY[1])
    else:
        print(WAY[2])
