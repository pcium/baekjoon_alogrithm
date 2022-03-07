import sys

score=[]
score_copy=[]
top5=[]
for i in range(8):
    score.append(int(sys.stdin.readline()))
score_copy = score[:]
score_copy.sort()
flag = score_copy[2]
print(sum(score_copy[3:]))
for i in range(8):
    if score[i] > flag:
        print(i+1, end=' ')
