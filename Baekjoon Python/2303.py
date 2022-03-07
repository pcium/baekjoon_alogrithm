import sys
from itertools import combinations

def onedigit(n):
    return n%10

N = int(sys.stdin.readline())
ppl = []
possible = []
result = []
winner = 0
for i in range(N):
    ppl.append(list(map(int, sys.stdin.readline().split())))
    possible.append(list(combinations(ppl[-1], 3)))
    result.append(max(map(onedigit, list(map(sum, possible[i])))))
for i in range(N):
    if result[i]==max(result):
        winner = i+1
print(winner)
    
