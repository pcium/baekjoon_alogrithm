import sys

H, W = map(int, sys.stdin.readline().split())
L = [[-1 for j in range(W)] for i in range(H)]
cloud = []
for i in range(H):
    temp = list(sys.stdin.readline().rstrip())
    cloud.append(temp)
for i in range(H):
    for j in range(W):
        if (cloud[i][j]) == 'c':
            for k in range(0, W-j):
                L[i][j+k] = k
for i in range(H):
    for j in range(W):
        print(L[i][j], end=' ')
    print()
