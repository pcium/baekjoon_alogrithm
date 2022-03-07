import sys
from collections import Counter

N = int(sys.stdin.readline())
valid = 0
for i in range(N):
    hello = list(sys.stdin.readline().rstrip())
    if (len(hello) == len(set(hello))):
        valid+=1
        continue
    counter = Counter(hello)
    counter = dict(counter)
    #print('Counter: ',counter)
    TR = 1
    for j in range(len(hello)):
        number = counter[hello[j]]
        #print('left: ', list(number*hello[j]))
        #print('right: ', hello[j:j+number])
        if number>=2 and list(number*hello[j]) != hello[j:j+number]:
            #print('Entered')
            TR = 0
            break
        counter[hello[j]] -= 1
    if TR == 1:
        valid+=1
print(valid)
