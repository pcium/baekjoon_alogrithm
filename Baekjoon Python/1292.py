import sys

A, B = map(int, sys.stdin.readline().split())
i=1
L = []
while (len(L)<=1000):
    for k in range(i):
        L.append(i)
    i+=1
print(sum(L[A-1:B]))
