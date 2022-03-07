import sys

# 중복까지 고려 필요 (같은 원소 count하여 + 해야할 듯)
N, K = map(int, sys.stdin.readline().split())
L = []
for i in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
L.sort(key=lambda x:(-x[1],-x[2],-x[3]))
save = []
rank = 0
for i in L:
    rank+=1
    popped = i.pop(0)
    if K == popped:
        save = i
    if save:
        rank-=1
        break
#print(L)
print(rank+1)

