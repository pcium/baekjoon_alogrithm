import sys
pattern=[]
stack = []
n = int(input())
for i in range(n):
    m = int(input())
    pattern.append(m)
max_idx = 0
pat_max = pattern[0]

for i in range(1,n):
    if pattern[i] > pat_max:
        max_idx = i
        pat_max = pattern[i]

# No 나오는 경우
for j in range(max_idx, n-1):
    if pattern[j] < pattern[j+1]:
        print("NO")
        sys.exit()
        
acc=0
now=0
for pt in pattern:
    while True:
        if acc<pt:
            acc += 1
            now = acc
            stack.append(acc)
            print('+')
        elif now>pt:
            now = stack.pop()
            print('-')
        elif now == pt:
            now = stack.pop()
            print('-')
            break
