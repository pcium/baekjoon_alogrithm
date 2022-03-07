import sys

classes = []
N = int(sys.stdin.readline())
for i in range(N):
    now = list(map(int, sys.stdin.readline().split()))
    length = now.pop(0)
    now.sort()
    gap = 0
    for j in range(length-1):
        gap = max(gap, now[j+1]-now[j])
    print('Class', i+1)
    print('Max {}, Min {}, Largest gap {}'.format(now[-1], now[0], gap))
    
