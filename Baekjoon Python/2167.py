import sys

data = []
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
manip = sum(data, [])

K =  int(sys.stdin.readline())
for r in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    for s in range(len(manip)):
        a = int(s/M)+1
        b = int(s%M)+1
        result = list(filter(lambda g : i<=a<=x and j<=b<=y, manip))
        print(result)
    print(sum(result))

