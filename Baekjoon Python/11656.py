import sys
S = sys.stdin.readline().rstrip()
B = []
for i in range(len(S)):
    B.append(S[i:])
B.sort()
for i in B:
    print(i)
