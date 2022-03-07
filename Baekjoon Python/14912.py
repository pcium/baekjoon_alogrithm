import sys

s = ''
n, d = map(int, sys.stdin.readline().split())
for i in range(1, n+1):
    s += str(i)
ls = list(s)
print(ls.count(str(d)))
