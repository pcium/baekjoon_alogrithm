import sys

A = [1, 2, 3, 4, 5]
B = list(map(int, sys.stdin.readline().split()))
while A != B:
    for i in range(4):
        if B[i] > B[i+1]:
            B[i], B[i+1] = B[i+1], B[i]
            for j in range(len(B)):
                print(B[j], end=' ')
            print()
