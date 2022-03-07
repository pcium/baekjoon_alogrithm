import sys

N = int(sys.stdin.readline())
L = list(set(map(int, sys.stdin.readline().split())))
L.sort()
for i in L:
    print(i, end=' ')
