import sys

N = int(sys.stdin.readline())
yaksu = list(map(int, sys.stdin.readline().split()))
yaksu.sort()
if N%2==0:
    print(yaksu[-1]*yaksu[0])
else:
    print(yaksu[N//2]**2)
