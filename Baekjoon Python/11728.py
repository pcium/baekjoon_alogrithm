import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A = list(A+B)
A.sort()
for i in A:
    print(i, end=' ')
