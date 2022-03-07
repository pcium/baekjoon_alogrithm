import sys

N, new_score, P = map(int, sys.stdin.readline().split()) # , 새 점수, 점수의 개수
if N==0:
    sys.exit()
scores = list(map(int, sys.stdin.readline().split()))

scores.append(new_score)
scores.sort(reverse=True)

if scores.index(new_score)==N:
    print(-1)
    sys.exit()
elif scores.index(new_score)==N-1 and scores.count(new_score)>1:
    print(-1)
    sys.exit()

print(scores.index(new_score)+1)

'''

for i in scores:
    if new_score>=i:
        rank=scores.index(i)
    
if rank==N+1:
    print(-1)
elif scores.count(scores[rank]) == 1:
    print(rank)
else:
    print(rank-scores.count(scores[rank])+1)

'''
