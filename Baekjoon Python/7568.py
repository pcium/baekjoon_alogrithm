N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
ans = []

for A in P:
    f = list(filter(lambda x: x[0] > A[0] and x[1] > A[1], P))
    ans.append(len(f)+1)

print(' '.join(list(map(str,ans))))
