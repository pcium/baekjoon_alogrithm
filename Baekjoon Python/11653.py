import sys

N = int(sys.stdin.readline())
if N==1:
    sys.exit()
yaksu = []
for i in range(2, N+1):
    if N % i == 0:
        yaksu.append(i)
j=0
while N!=1:
    if N % yaksu[j] == 0:
        N /= yaksu[j]
        print(yaksu[j])
        continue
    j+=1
