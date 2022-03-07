import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)
accum = 0
for i in A:
    if i==0:
        a=A.pop(0)
        b=B.pop(0)

A.sort(reverse=True)
B.sort()
for i in B:
    if i==0:
        a=A.pop(0)
        b=B.pop(0)

for i in range(len(A)):
    accum+=(A[i]*B[i])
print(accum)
