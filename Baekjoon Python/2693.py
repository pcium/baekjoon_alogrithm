import sys

T = int(sys.stdin.readline())
for i in range(T):
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    print(lst[-3])
