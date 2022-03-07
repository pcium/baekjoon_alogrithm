import sys
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

A = list(map(int, sys.stdin.readline().rstrip().split(':')))
G = gcd(A[0], A[1])
print('{}:{}'.format(int(A[0]/G),int(A[1]/G)))

