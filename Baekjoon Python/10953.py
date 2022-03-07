import sys

T = int(sys.stdin.readline())
for i in range(T):
    A = list(map(int, sys.stdin.readline().split(',')))
    print(sum(A))
