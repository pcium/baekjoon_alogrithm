import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))
T.sort(reverse=True)
for i in range(len(T)):
    T[i] = T[i] + (i+2)
print(max(T))
