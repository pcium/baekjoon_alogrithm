import sys

N = sys.stdin.readline().rstrip()
for i in sorted(list(N), reverse = True):
    print(i, end='')
