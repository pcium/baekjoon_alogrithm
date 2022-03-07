import sys
N = int(sys.stdin.readline()) # 분해합 결과
n = N
digit=1

while True:
    if int(n/10) ==  0:
        break
    else:
        n/=10
        digit += 1
        
origin = 0

for i in range(N-9*digit, N): # 후보 테스트
    if i<=0:
        continue
    dgts = list(map(int, list(str(i))))
    if (i+sum(dgts) == N):
        origin = i
        break

print(origin)
    
